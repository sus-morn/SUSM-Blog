from fastapi import FastAPI

app = FastAPI(title="SUSM Blog", description="A simple blog API", version="0.0.1")

@app.get("/")
async def root():
    return {"message": "Welcome to SUSM Blog API!"}
