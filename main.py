import graphene
from sqlalchemy import create_engine
from graphene_sqlalchemy import SQLAlchemyObjectType
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from models import *

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        # only return specified fields
        only_fields = ("name",)
        # exclude specified fields
        exclude_fields = ("last_name",)

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        query = User.get_query(info)  # SQLAlchemy query
        return query.all()

app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
