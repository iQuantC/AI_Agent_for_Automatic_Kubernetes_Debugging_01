import subprocess

def apply_fix(pod_name):
    print(f" Applying fix to {pod_name}...")

    cmd = [
        "kubectl", "set", "resources", "deployment", "faulty-app",
        "--limits=memory=128Mi"
    ]

    subprocess.run(cmd, check=True, capture_output=True, text=True)
