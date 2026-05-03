import fastapi,time
from router import route_request
from cache import get_from_cache, save_to_cache
from pydantic import BaseModel

class Query(BaseModel):
    query: str

app = fastapi.FastAPI()


@app.get("/")
def health_check():
    return {"status": "Adaptive API is running"}

@app.post("/query")
def classify_route(query: Query):
    start_time = time.time()
    temp_cache= get_from_cache(query.query)
    if temp_cache:
        temp_cache["latency_ms"] = round((time.time() - start_time) * 1000, 2)
        return temp_cache
    response = route_request(query.query)
    result={
        "service":response[0],
        "response":response[1],
        "latency_ms":round((time.time() - start_time) * 1000, 2)
    }
    save_to_cache(query.query, result.copy())
    return result