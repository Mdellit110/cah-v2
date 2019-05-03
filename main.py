import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from models import *

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

class WhiteCard(SQLAlchemyObjectType):
    class Meta:
        model = WhiteCardModel

class BlackCard(SQLAlchemyObjectType):
    class Meta:
        model = BlackCardModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        query = User.get_query(info)  # SQLAlchemy query
        return query.all()


app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
