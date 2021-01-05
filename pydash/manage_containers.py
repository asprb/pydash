import docker

client = docker.from_env()

def restart_container():
    pass

def get_by_status(status=None):
    if status is None:
        return client.containers.list()
    else:
        return client.containers.list(filters={status: status})
        