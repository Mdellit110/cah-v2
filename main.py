import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from models import *

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )

class UserConnection(relay.Connection):
    class Meta:
        node = User

class WhiteCard(SQLAlchemyObjectType):
    class Meta:
        model = WhiteCardModel
        interfaces = (relay.Node, )

class WhiteCardConnection(relay.Connection):
    class Meta:
        node = WhiteCard

class BlackCard(SQLAlchemyObjectType):
    class Meta:
        model = BlackCardModel
        interfaces = (relay.Node, )

class BlackCardConnection(relay.Connection):
    class Meta:
        node = BlackCard

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserConnection)
    all_blackcards = SQLAlchemyConnectionField(BlackCardConnection)
    all_whitecards = SQLAlchemyConnectionField(WhiteCardConnection)


app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
