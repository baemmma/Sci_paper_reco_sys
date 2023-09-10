from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def generate_recommendations(query, papers):
    query_embedding = model.encode([query])[0]
    paper_embeddings = []

    for paper in papers:
        paper_embedding = model.encode([paper['abstract']])[0]
        paper_embeddings.append(paper_embedding)

    paper_embeddings = np.array(paper_embeddings)
    similarity_scores = cosine_similarity([query_embedding], paper_embeddings)[0]

    sorted_indices = np.argsort(similarity_scores)[::-1]
    sorted_recommendations = [papers[i] for i in sorted_indices]

    return sorted_recommendations
