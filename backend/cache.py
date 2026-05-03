# cache.py
cache = {}


def get_from_cache(query: str):
    return cache.get(query)


def save_to_cache(query: str, response: dict):
    cache[query] = response