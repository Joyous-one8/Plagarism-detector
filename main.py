from sentence_transformers import SentenceTransformer, util
import torch

def compute_similarity(text1, text2):
    # Load the sentence transformer model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode([text1, text2], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    return float(similarity.item())

def is_plagiarized(text1, text2, threshold=0.8):
    similarity_score = compute_similarity(text1, text2)
    return {
        'similarity_score': round(similarity_score, 4),
        'plagiarized': similarity_score >= threshold
    }

if __name__ == '__main__':
    print("=== Semantic Plagiarism Detector ===")
    
    original = input("Enter original text:\n")
    suspect = input("\nEnter suspected plagiarized text:\n")
    
    try:
        threshold = float(input("\nEnter similarity threshold (e.g., 0.8): "))
    except ValueError:
        threshold = 0.8
        print("Invalid input. Using default threshold of 0.8.")

    result = is_plagiarized(original, suspect, threshold)
    
    print("\n--- Results ---")
    print(f"Similarity Score: {result['similarity_score']}")
    print("Plagiarized." if result['plagiarized'] else "Not Plagiarized.")
