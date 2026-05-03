import fastapi
import cache
from services.ai_service import call_ai_service
from services.search_service import search_service
from services.fallback_service import call_fallback_service


def route_request(query: str):
    search_keywords = ["search", "find", "look", "get", "fetch", "list", "show", "display"]
    ai_keywords = ["ai", "intelligence", "smart", "cognitive", "neural", "learning", "predict", "classify", "analyze", "recommend", "suggest", "evaluate", "assess", "diagnose", "forecast", "estimate", "optimize", "plan", "schedule", "allocate", "assign", "manage", "coordinate", "control", "regulate", "monitor", "supervise", "guide", "assist", "support", "help"]

    query = query.lower()

    for keyword in search_keywords:
        if keyword in query:
            return "search", search_service(query)
    
    for keyword in ai_keywords:
        if keyword in query:
            return "ai", call_ai_service(query)
    
    return "fallback", call_fallback_service(query)


    
