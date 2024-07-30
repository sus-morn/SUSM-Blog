from fastapi import FastAPI,Depends

from database import session_local, engine, User, Article
app = FastAPI(title="SUSM Blog", description="A simple blog API", version="0.0.1")

# 未来移入Dependency
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to SUSM Blog API!"}

@app.post("/article/post")
async def post_article( content: str, db = Depends(get_db)):
    db.add(Article(title="test", content=content, author_id=1))
    db.commit()
    return content

@app.get("/article/{article_id}")
async def get_article(article_id: int, db = Depends(get_db)):
    data = db.query(Article).filter(Article.id == article_id).first()
    return data.content