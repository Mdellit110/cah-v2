import graphene
from graphene import relay, Union, List
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from starlette.middleware.cors import CORSMiddleware
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

class SearchResult(Union):
    class Meta:
        types = (WhiteCard, BlackCard)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    search = List(SearchResult, deck=graphene.String(), text=graphene.String())
    all_users = SQLAlchemyConnectionField(UserConnection)
    all_blackcards = SQLAlchemyConnectionField(BlackCardConnection)
    all_whitecards = SQLAlchemyConnectionField(WhiteCardConnection)

    def resolve_search(self, info, **args):
        whitecard_query = WhiteCard.get_query(info)
        blackcard_query = BlackCard.get_query(info)

        if "deck" in args.keys():
            q = args.get("deck")
            whiteCards = whitecard_query.filter((WhiteCardModel.deck.contains(q))).all()
            blackCards = blackcard_query.filter((BlackCardModel.deck.contains(q))).all()
        elif "text" in args.keys():
            q = args.get("text")
            whiteCards = whitecard_query.filter((WhiteCardModel.text.contains(q))).all()
            blackCards = blackcard_query.filter((BlackCardModel.text.contains(q))).all()

        return whiteCards + blackCards

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query, types=[WhiteCard, BlackCard, SearchResult])))
