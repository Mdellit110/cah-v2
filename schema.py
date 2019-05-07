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
    search = List(SearchResult, deck=graphene.String(), text=graphene.String())
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

schema=graphene.Schema(query=Query, types=[WhiteCard, BlackCard, SearchResult])
