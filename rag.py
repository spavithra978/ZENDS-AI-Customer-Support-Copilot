from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from policy_data import policies

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

policy_embeddings = embedding_model.encode(
    policies
)

dimension = policy_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(
    np.array(policy_embeddings)
)

def retrieve_policy(query):

    query_embedding = embedding_model.encode(
        [query]
    )

    D, I = index.search(
        np.array(query_embedding),
        k=1
    )

    return policies[I[0][0]]