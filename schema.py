import graphene
from graphene import relay, Union, List
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from database.models import *
from schema_whitecards import *
from schema_blackcards import *

class SearchResult(Union):
    class Meta:
        types = (WhiteCard, BlackCard)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    white_decks = List(WhiteCard, deck=graphene.List(graphene.String), text=graphene.String())
    black_decks = List(BlackCard, deck=graphene.List(graphene.String), text=graphene.String())

    def resolve_white_decks(self, info, **args):
        whitecard_query = WhiteCard.get_query(info)
        q = args.get("deck")
        whiteCards = []
        if "deck" in args.keys():
            for arg in q:
                whiteCards.extend(whitecard_query.filter((WhiteCardModel.deck.contains(arg))))

        if "text" in args.keys():
            q = args.get("text")
            whiteCards.extend(whitecard_query.filter((WhiteCardModel.text.contains(q))).all())

        return whiteCards

    def resolve_black_decks(self, info, **args):
        blackcard_query = BlackCard.get_query(info)
        q = args.get("deck")
        blackCards = []
        if "deck" in args.keys():
            for arg in q:
                blackCards.extend(blackcard_query.filter((BlackCardModel.deck.contains(arg))))

        if "text" in args.keys():
            q = args.get("text")
            blackCards.extend(blackcard_query.filter((BlackCardModel.text.contains(q))).all())


        return blackCards



schema=graphene.Schema(query=Query, types=[WhiteCard, BlackCard])
