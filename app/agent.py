from vector_store import query_knowledge, load_knowledge
from k8s_collector import get_pod_logs, get_pod_status
from fixer import apply_fix
import ollama
import warnings
warnings.filterwarnings("ignore")

def diagnose():
    load_knowledge()
    logs = get_pod_logs()
    statuses = get_pod_status()

    for pod, log in logs:
        print(f"\n Analyzing Pod: {pod}")

        context = query_knowledge(log)

        prompt = f"""
        Pod Logs:
        {log}

        Knowledge:
        {context}

        Diagnose the issue and suggest a fix.
        """

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        answer = response['message']['content']
        print("Diagnosis:", answer)

        trigger_keywords = ["increase memory", "oomkilled", "memory limit", "resource", "out of memory"]
        if any(kw in answer.lower() for kw in trigger_keywords):
            apply_fix(pod)

if __name__ == "__main__":
    diagnose()
