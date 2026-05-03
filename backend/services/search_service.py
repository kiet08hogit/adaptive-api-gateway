def search_service(query: str):
    return {
        "message": f"Search service matched results for: {query}",
        "results": [
            "Result 1: API Gateway design pattern",
            "Result 2: Caching strategy for backend systems",
            "Result 3: AI routing architecture"
        ]
    }