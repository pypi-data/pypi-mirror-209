import logging
import re
import docker
import requests
import base64
import json
import signal
import pathlib

from dateutil.parser import parse
from docker.client import DockerClient
from docker.models.containers import Container
from docker.models.networks import Network
from typing import Dict, Union

from vantage6.common import logger_name
from vantage6.common import ClickLogger
from vantage6.common.globals import APPNAME

log = logging.getLogger(logger_name(__name__))

docker_client = docker.from_env()


class ContainerKillListener:
    """Listen for signals that the docker container should be shut down """
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill_now = True


def check_docker_running():
    """Return True if docker engine is running"""
    try:
        docker_client.ping()
    except Exception as e:
        log.error("Cannot reach the Docker engine! Please make sure Docker "
                  "is running.")
        log.warn("Exiting...")
        log.debug(e)
        exit(1)


def running_in_docker() -> bool:
    """Return True if this code is executed within a Docker container."""
    return pathlib.Path('/.dockerenv').exists()


def registry_basic_auth_header(docker_client, registry):
    """Obtain credentials for registry

    This is a wrapper around docker-py to obtain the credentials used
    to access a registry. Normally communication to the registry goes
    through the Docker deamon API (locally), therefore we have to take
    extra steps in order to communicate with the (Harbor) registry
    directly.

    Note that this has only been tested for the harbor registries.

    Parameters
    ----------
    registry : str
        registry name (e.g. harbor.vantage6.ai)

    Returns
    -------
    dict
        Containing a basic authorization header
    """

    # Obtain the header used to be send to the docker deamon. We
    # communicate directly with the registry therefore we need to
    # change this headers.
    header = docker.auth.get_config_header(docker_client.api, registry)
    if not header:
        log.debug(f'No credentials found for {registry}')
        return

    # decode header
    header_json = json.loads(base64.b64decode(header))

    # Extract username and password. Depending on the docker version, the keys
    # may be capitalized in the JSON header
    username = header_json['username'] if 'username' in header_json \
        else header_json['Username']
    password = header_json['password'] if 'password' in header_json \
        else header_json['Password']
    basic_auth = f"{username}:{password}"

    # Encode them back to base64 and as a dict
    bytes_basic_auth = basic_auth.encode("utf-8")
    b64_basic_auth = base64.b64encode(bytes_basic_auth).decode("utf-8")

    return {'authorization': f'Basic {b64_basic_auth}'}


def inspect_remote_image_timestamp(docker_client, image: str, log=ClickLogger):
    """
    Obtain creation timestamp object from remote image.

    Parameters
    ----------
    reg : str
        registry where the image is hosted
    rep : str
        repository in the registry
    img : str
        image name
    tag : str, optional
        image tag to be used, by default "latest"

    Returns
    -------
    datetime
        timestamp object containing the creation date and time of the image
    """
    # check if a tag has been profided

    image_tag = re.split(":", image)
    img = image_tag[0]
    tag = image_tag[1] if len(image_tag) == 2 else "latest"

    try:
        reg, rep, img_ = re.split("/", img)
    except ValueError:
        log.warn("Could not construct remote URL, "
                 "are you using a local image?")
        log.warn("Or an image from docker hub?")
        log.warn("We'll make a final attempt when running the image to pull"
                 " it without any checks...")
        return

    # figure out API of the docker repo
    v1_check = requests.get(f"https://{reg}/api/health")
    v1 = v1_check.status_code == 200
    v2 = False
    if not v1:
        v2_check = requests.get(f"https://{reg}/api/v2.0/health")
        v2 = v2_check.status_code == 200

    if not v1 and not v2:
        log.error(f"Could not determine version of the registry! {reg}")
        log.error("Is this a Harbor registry?")
        log.error("Or is the harbor server offline?")
        return

    if v1:
        image = f"https://{reg}/api/repositories/{rep}/{img_}/tags/{tag}"
    else:
        image = f"https://{reg}/api/v2.0/projects/{rep}/repositories/" \
                f"{img_}/artifacts/{tag}"

    # retrieve info from the Harbor server
    result = requests.get(
        image, headers=registry_basic_auth_header(docker_client, reg)
    )

    # verify that we got an result
    if result.status_code == 404:
        log.warn(f"Remote image not found! {image}")
        return

    if result.status_code != 200:
        log.warn(f"Remote info could not be fetched! ({result.status_code}) "
                 f"{image}")
        return

    if v1:
        timestamp = parse(result.json().get("created"))
    else:
        timestamp = parse(result.json().get("push_time"))
    return timestamp


def inspect_local_image_timestamp(docker_client, image: str, log=ClickLogger):
    """
    Obtain creation timestamp object from local image.

    Parameters
    ----------
    reg : str
        registry where the image is hosted
    rep : str
        repository in the registry
    img : str
        image name
    tag : str, optional
        image tag to be used, by default "latest"

    Returns
    -------
    datetime
        timestamp object containing the creation date and time of the image
    """
    # p = re.split(r"[/:]", image)
    # if len(p) == 4:
    #     image = f"{p[0]}/{p[1]}/{p[2]}:{p[3]}"

    try:
        img = docker_client.images.get(image)
    except docker.errors.ImageNotFound:
        log.debug(f"Local image does not exist! {image}")
        return None
    except docker.errors.APIError:
        log.debug(f"Local info not available! {image}")
        return None

    timestamp = img.attrs.get("Created")
    timestamp = parse(timestamp)
    return timestamp


def pull_if_newer(docker_client: DockerClient, image: str,
                  log: Union[logging.Logger, ClickLogger] = ClickLogger):
    """
    Docker pull only if the remote image is newer.

    Parameters
    ----------
    docker_client: DockerClient
        A Docker client instance
    image: str
        Image to be pulled
    log: logger.Logger or ClickLogger
        Logger class
    """
    local_ = inspect_local_image_timestamp(docker_client, image, log=log)
    remote_ = inspect_remote_image_timestamp(docker_client, image, log=log)
    pull = False
    if local_ and remote_:
        if remote_ > local_:
            log.debug(f"Remote image is newer: {image}")
            pull = True
        elif remote_ == local_:
            log.debug(f"Local image is up-to-date: {image}")
        elif remote_ < local_:
            log.warn(f"Local image is newer! Are you testing? {image}")
    elif local_:
        log.warn(f"Only a local image has been found! {image}")
    elif remote_:
        log.debug("No local image found, pulling from remote!")
        pull = True
    elif not local_ and not remote_:
        log.warn(f"Cannot locate image {image} locally or remotely. Will try "
                 "to pull it from Docker Hub...")
        # we will try to pull it from the docker hub
        pull = True

    if pull:
        try:
            docker_client.images.pull(image)
            log.debug(f"Succeeded to pull image: {image}")
        except docker.errors.APIError as e:
            log.error(f"Failed to pull image! {image}")
            log.debug(e)
            raise docker.errors.APIError("Failed to pull image") from e


def get_container(docker_client: DockerClient, **filters) -> Container:
    """
    Return container if it exists after searching using kwargs

    Parameters
    ----------
    docker_client: DockerClient
        Python docker client
    **filters:
        These are arguments that will be passed to the client.container.list()
        function. They should yield 0 or 1 containers as result (e.g.
        name='something')

    Returns
    -------
    Container or None
        Container if it exists, else None
    """
    running_containers = docker_client.containers.list(
        all=True, filters=filters
    )
    return running_containers[0] if running_containers else None


def remove_container_if_exists(docker_client: DockerClient, **filters) -> None:
    """
    Kill and remove a docker container if it exists

    Parameters
    ----------
    docker_client: DockerClient
        A Docker client
    **filters:
        These are arguments that will be passed to the client.container.list()
        function. They should yield 0 or 1 containers as result (e.g.
        name='something')
    """
    container = get_container(docker_client, **filters)
    if container:
        log.warn("Removing container that was already running: "
                 f"{container.name}")
        remove_container(container, kill=True)


def remove_container(container: Container, kill=False) -> None:
    """
    Removes a docker container

    Parameters
    ----------
    container: Container
        The container that should be removed
    kill: bool
        Whether or not container should be killed before it is removed
    """
    if kill:
        # TODO it would be nice to observe container status before attempting
        # to kill it, so that we do not have to pass Exceptions
        try:
            container.kill()
        except Exception:
            pass  # allow failure here, maybe container had already exited
    try:
        container.remove()
    except Exception as e:
        log.exception(f"Failed to remove container {container.name}")
        log.debug(e)


def get_network(docker_client: DockerClient, **filters) -> Network:
    """ Return network if it exists after searching using kwargs

    Parameters
    ----------
    docker_client: DockerClient
        Python docker client
    **filters:
        These are arguments that will be passed to the client.network.list()
        function. They should yield 0 or 1 networks as result (e.g.
        name='something')

    Returns
    -------
    Container or None
        Container if it exists, else None
    """
    networks = docker_client.networks.list(
        filters=filters
    )
    return networks[0] if networks else None


def delete_network(network: Network, kill_containers: bool = True) -> None:
    """ Delete network and optionally its containers

    Parameters
    ----------
    network: Network
        Network to delete
    kill_containers: bool
        Whether to kill the containers in the network (otherwise they are
        merely disconnected)
    """
    if not network:
        log.warn("Network not defined! Not removing anything, continuing...")
        return
    network.reload()
    for container in network.containers:
        log.info(f"Removing container {container.name} in old network")
        if kill_containers:
            log.warn(f"Killing container {container.name}")
            remove_container(container, kill=True)
        else:
            network.disconnect(container)
    # remove the network
    try:
        network.remove()
    except Exception:
        log.warn(f"Could not delete existing network {network.name}")


def get_networks_of_container(container: Container) -> Dict:
    """
    Get list of networks the container is in

    Parameters
    ----------
    container: Container
        The container in which we are interested

    Returns
    -------
    dict
        Describes container's networks and their properties
    """
    container.reload()
    return container.attrs['NetworkSettings']['Networks']


def get_num_nonempty_networks(container: Container) -> int:
    """
    Get number of networks the container is in where it is not the only one

    Parameters
    ----------
    container: Container
        The container in which we are interested

    Returns
    -------
    int
        Number of networks in which the container resides in which there are
        also other containers
    """
    count_non_empty_networks = 0

    networks = get_networks_of_container(container)
    for network_properties in networks.values():
        network_obj = docker_client.networks.get(
            network_properties['NetworkID']
        )
        if not network_obj:
            continue
        containers = network_obj.attrs['Containers']
        if len(containers) > 1:
            count_non_empty_networks += 1
    return count_non_empty_networks


def get_server_config_name(container_name: str, scope: str):
    """
    Get the configuration name of a server from its docker container name

    Docker container name of the server is formatted as
    f"{APPNAME}-{self.name}-{self.scope}-server". This will return {self.name}

    Parameters
    ----------
    container_name: str
        Name of the docker container in which the server is running
    scope: str
        Scope of the server (e.g. 'system' or 'user')

    Returns
    -------
    str
        A server's configuration name
    """
    idx_scope = container_name.rfind(scope)
    length_app_name = len(APPNAME)
    return container_name[length_app_name+1:idx_scope-1]
