from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

def get_pod_logs():
    pods = v1.list_namespaced_pod(namespace="default")
    logs = []

    for pod in pods.items:
        try:
            log = v1.read_namespaced_pod_log(
                name=pod.metadata.name,
                namespace="default"
            )
            logs.append((pod.metadata.name, log))
        except Exception as e:
            logs.append((pod.metadata.name, str(e)))

    return logs

def get_pod_status():
    pods = v1.list_namespaced_pod(namespace="default")
    status = []

    for pod in pods.items:
        status.append((pod.metadata.name, pod.status.phase))

    return status
