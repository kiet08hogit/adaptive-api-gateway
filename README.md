# Adaptive API Gateway

A high-performance FastAPI backend featuring a **Semantic Cache** powered by Sentence Transformers.

## 🚀 Getting Started (Docker)

If you have Docker installed, you can get the entire system running with a single command. This will build the Python environment and the Semantic Cache model automatically.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kiet08hogit/adaptive-api-gateway.git
   cd adaptive-api-gateway
   ```

2. **Run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

The API will be available at **http://localhost:8000**.

## 🛠️ Local Development (No Docker)

If you prefer to run it locally without Docker:

1. **Navigate to backend and create a virtual environment:**
   ```bash
   cd backend
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Mac/Linux
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

3. **Run the server:**
   ```bash
   python -m uvicorn main:app --reload
   ```

## 🧪 Testing

We use `pytest` for automated testing. To run tests:
```bash
cd backend
python -m pytest
```

## 📈 Features
- **Semantic Caching**: Uses `all-MiniLM-L6-v2` embeddings to identify similar queries and serve cached results even if the wording is different.
- **Adaptive Routing**: Automatically routes requests to AI, Search, or Fallback services based on query keywords.
- **CI/CD Ready**: Automated testing and deployment to Render via GitHub Actions. (currently disable due to cost)
