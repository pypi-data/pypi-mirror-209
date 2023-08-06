# ----------------------------------------------------------------------------
# ShipHelm Copyright 2020-2023 by Gameplex Software and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------
import docker



class helmswarm:
    def __init__(self, remote_address=None, remote_is_TLS=None):
        try:
            pass
        except:
            helmswarm.client = docker.DockerClient(base_url=remote_address, tls=remote_is_TLS)

    def get_running_containers(self):
        return helmswarm.client.containers.list()

    def get_container_by_id(self, container_id):
        return helmswarm.client.containers.get(container_id)

    def get_container_stats(self, container_id):
        container = helmswarm.client.containers.get(container_id)
        stats = container.stats(stream=False)
        return stats

    def get_container_ports(self, container_id):
        container = helmswarm.client.containers.get(container_id)
        ports = container.attrs['NetworkSettings']['Ports']
        return ports

    def search_containers(self, name):
        return helmswarm.client.containers.list(filters={"name": name})

    def change_container_ports(self, container_id, ports):
        container = helmswarm.client.containers.get(container_id)
        container.reload()
        container.ports.update(ports)

    def rename_container(self, container_id, new_name):
        container = helmswarm.client.containers.get(container_id)
        container.rename(new_name)

    def add_container_to_network(self, container_id, network_name):
        network = helmswarm.client.networks.get(network_name)
        container = helmswarm.client.containers.get(container_id)
        network.connect(container)

    def remove_container_from_network(self, container_id, network_name):
        network = helmswarm.client.networks.get(network_name)
        container = helmswarm.client.containers.get(container_id)
        network.disconnect(container)

    def create_network(self, network_name):
        helmswarm.client.networks.create(network_name)

    def delete_network(self, network_name):
        network = helmswarm.client.networks.get(network_name)
        network.remove()

    def run_container(self, image, command=None, detach=False, ports=None, environment=None, volumes=None):
        container = helmswarm.client.containers.run(
            image=image,
            command=command,
            detach=detach,
            ports=ports,
            environment=environment,
            volumes=volumes
        )
        return container

    def get_container_environment(self, container_id):
        container = helmswarm.client.containers.get(container_id)
        environment = container.attrs['Config']['Env']
        return environment

    def set_container_environment(self, container_id, environment):
        container = helmswarm.client.containers.get(container_id)
        container.reload()
        container.update(env=environment)

    def get_container_volumes(self, container_id):
        container = helmswarm.client.containers.get(container_id)
        volumes = container.attrs['HostConfig']['Binds']
        return volumes

    def set_container_volumes(self, container_id, volumes):
        container = helmswarm.client.containers.get(container_id)
        container.reload()
        container.update(binds=volumes)
