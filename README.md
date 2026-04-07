# DevOps AI Agent for Automatic Kubernetes Debugging 101
In this project, we build an end-to-end AI-powered DevOps Agent that monitors Kubernetes cluster, collects logs from pods, stores knowledge in a vector DB, and uses an AI Agent to diagnose the issues, suggest fixes and apply  the fixes automatically. 

## Tech Stack
1. Kubernetes (Minikube)
2. Python
3. LangChain
4. HuggingFace Embeddings
5. Open-source LLM (e.g. via Ollama)
6. Kubectl CLI

```sh
mkdir app data k8s
```

## Step 1: Set up Python Virtual Environment
```sh
python -m venv devops_agent
source devops_agent/bin/activate
```

```sh
pip install -r requirements.txt
```

## Step 2: Setup Kubernetes Cluster
Make sure that Minikube is installed on your system

```sh
minikube start
kubectl get nodes
```

## Step 3: Knowledge Base
Here we will create a knowledge base for our agent

```sh
mkdir data && cd data
touch knowledge_base.txt
```

## Step 4: Vector Store (Chroma)

```sh
mkdir app && cd app
touch vector_store.py
touch k8s_collector.py
touch fixer.py
```

## Step 5: Run the Agent
Be sure that you have a HuggingFace Account and login via cli:
```sh
pip install --upgrade huggingface_hub
pip show huggingface_hub
python -m huggingface_hub.cli.hf auth login
```

OR 

You can also add this to your .bashrc file as follows:
```sh
vim ~/.bashrc
```

Add the following to the .bashrc file:
```sh
# Add to your ~/.bashrc or ~/.zshrc
alias hf="python -m huggingface_hub.cli.hf"
```
To check it:
```sh
which hf
hf auth login
```

### Create HuggingFace Token
1. Login to HuggingFace Account
2. Go to settings, and access tokens
3. Create new token.    Name: cli login
                        Permissions: "Write". Generate token.
4. Copy and Paste token on terminal and press Enter
5. Add token as git cred: No. Press enter


## Step 6: Deploy a Faulty App (for testing)
Deploy a Faulty App with low memory (intentionally low)
```sh 
kubectl apply -f k8s/faulty-app.yaml
kubectl get all
```

Grab the URL of App and open it on your browser:
```sh
minikube service faulty-app-service
```


Check the Kubernetes pods of the Faulty App on a dedicated terminal:
```sh
kubectl get pods
kubectl describe pod <pod_name>
```

Let's watch it as we apply a fix using our AI Agent:
```sh
kubectl get pods --watch
kubectl get deploy --watch
```

Run the Agent
```sh
python app/agent.py
```
You will see the changes been done real-time. 
Verify that it is "READY" by checking the status of the pod or deployment
```sh
kubectl get all
```

Re-run the app URL on your browser to see that the fix worked!

### Clean UP

```sh
kubectl delete deploy faulty-app
kubectl delete svc faulty-app-service
kubectl get all
```

```sh
minikube stop
minikube delete
```

## PLEASE LIKE, COMMENT, and SUBSCRIBE
