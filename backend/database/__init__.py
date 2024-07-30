from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

session_local = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()

# 以下未来要移植到model.py

class User(Base):
    
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,unique=True,autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    articles = relationship("Article", back_populates="author")
    permissions = Column(Integer, default=1)
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

class Article(Base):
    
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True,unique=True,autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="articles")
    
    def __repr__(self):
        return f"<Article(title='{self.title}')>"

Base.metadata.create_all(bind=engine)