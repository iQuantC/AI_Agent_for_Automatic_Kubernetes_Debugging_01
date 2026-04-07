import chromadb
from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

client = chromadb.Client()
collection = client.create_collection(name="k8s-debug")

def load_knowledge():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(base_dir, "data", "knowledge_base.txt")) as f:
        docs = f.readlines()

    for i, doc in enumerate(docs):
        embedding = model.encode(doc).tolist()
        collection.add(
            documents=[doc],
            embeddings=[embedding],
            ids=[str(i)]
        )

def query_knowledge(query):
    embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=2)
    return results["documents"]
