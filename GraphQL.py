from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import  strawberry
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

#Database setup
DATABASE_URL = "sqlite:///:memory:?check_same_thread=False"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

#GraphQL Schema
@strawberry.type
class User:
    id: int
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def users(self) ->List[User]:
        db = SessionLocal()
        users = db.query(UserModel).all()
        db.close()
        return [User(id=u.id, name=u.name, email=u.email) for u in users]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, name: str, email: str) -> User:
        db = SessionLocal()
        new_user = UserModel(name=name, email=email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.close()
        return User(id=new_user.id, name=new_user.name, email=new_user.email)

#FastAPI
app = FastAPI()

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")