from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Adaptive API is running"}

def test_query_route_search():
    response = client.post("/query", json={"query": "how to search for an item"})
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "search"
    assert "response" in data
    assert data.get("cache_hit", False) is False

def test_query_route_ai():
    response = client.post("/query", json={"query": "can you analyze this data"})
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "ai"

def test_query_route_fallback():
    response = client.post("/query", json={"query": "something completely random"})
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "fallback"

def test_semantic_cache_hit():
    # 1. First query to populate the cache
    query1 = "how do I run the server"
    res1 = client.post("/query", json={"query": query1})
    assert res1.status_code == 200
    assert res1.json().get("cache_hit", False) is False

    # 2. Exact same query should definitely hit the cache
    res2 = client.post("/query", json={"query": query1})
    assert res2.status_code == 200
    data2 = res2.json()
    assert data2["cache_hit"] is True
    assert data2["semantic_cache_hit"] is True
    assert data2["similarity_score"] > 0.99
