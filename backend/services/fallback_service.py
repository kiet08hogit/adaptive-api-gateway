def call_fallback_service(query: str):
    return {
        "message": f"Fallback service called for query: {query}",
        "note": "The backend system could not classify this request, please try again."
    }
    
