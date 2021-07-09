import docker


class Cluster:
    """
    Container for holding cluster's information
    """
    def __init__(self, primary_name, standby_names):
        client = docker.from_env()
        self._primary = client.containers.get(primary_name)
        self._standbys = [client.containers.get(name) for name in standby_names]

    def get_standby_count(self):
        return len(self._standbys)

    def get_primary_ip(self):
        return self._primary.attrs['NetworkSettings']['IPAddress']

    def get_standby_ips(self):
        return [standby.attrs['NetworkSettings']['IPAddress'] for standby in self._standbys]

    def remove_all_nodes(self):
        self._primary.stop()
        self._primary.remove()
        for standby in self._standbys:
            standby.stop()
            standby.remove()
