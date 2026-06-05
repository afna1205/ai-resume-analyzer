from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Copilot",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Project Started"}