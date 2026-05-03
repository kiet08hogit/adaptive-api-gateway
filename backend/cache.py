
from sentence_transformers import SentenceTransformer
import time
import numpy as np
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
cache = {}
THRESHOLD = 0.75

def embedding_queries(query:str):
    normalized_query=query.lower()
    return embedding_model.encode(normalized_query)


def similarity_score(vector1,vector2):
    return np.dot(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2))


def get_from_cache(query: str):
    query_embedding=embedding_queries(query)
    best_match = None
    best_score = 0
    for cached_query, cached_response in cache.items():
        cached_embedding=cached_response["embedding"]
        score=similarity_score(query_embedding,cached_embedding)
        if score>best_score:
            best_score=score
            best_match=cached_response
    if best_score>THRESHOLD:
        result = best_match["result"].copy()
        result["cache_hit"] = True
        result["semantic_cache_hit"] = True
        result["matched_query"] = best_match["query"]
        result["similarity_score"] = round(float(best_score), 3)
        return result
    return None


def save_to_cache(query: str, response: dict):
    cache[query]={
        "query":query,
        "embedding":embedding_queries(query),
        "result":response,
        "timestamp":time.time()
    }