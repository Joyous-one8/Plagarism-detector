import os
from sentence_transformers import SentenceTransformer, util

# Initialize model
model = SentenceTransformer('all-MiniLM-L6-v2')

SIMILARITY_THRESHOLD = 0.85  # Adjust based on sensitivity

# Read all files from a folder
def load_documents_from_folder(folder_path):
    docs = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                docs[filename] = file.read()
    return docs

# Compare all pairs and return results
def calculate_pairwise_similarity(docs):
    names = list(docs.keys())
    embeddings = model.encode([docs[name] for name in names], convert_to_tensor=True)
    results = []

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            sim_score = util.cos_sim(embeddings[i], embeddings[j]).item()
            results.append((names[i], names[j], sim_score))
    return results

# Function to be called from UI or script
def check_plagiarism_in_folder(folder_path, threshold=SIMILARITY_THRESHOLD):
    documents = load_documents_from_folder(folder_path)
    scores = calculate_pairwise_similarity(documents)

    results = []
    for doc1, doc2, score in scores:
        if score >= threshold:
            results.append({
                "file1": doc1,
                "file2": doc2,
                "score": round(score, 4)
            })
    return results

# CLI Mode
if __name__ == "__main__":
    FOLDER_PATH = "reports"  # or any folder path you want
    documents = load_documents_from_folder(FOLDER_PATH)
    if len(documents) < 2:
        print("Need at least 2 text files in the folder to compare.")
    else:
        scores = calculate_pairwise_similarity(documents)
        for doc1, doc2, score in scores:
            if score >= SIMILARITY_THRESHOLD:
                print(f"\n🚨 Plagiarism Alert: {doc1} and {doc2}")
                print(f"Semantic Similarity Score: {score:.4f}")
