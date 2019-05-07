import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.models import *

class WhiteCard(SQLAlchemyObjectType):
    class Meta:
        model = WhiteCardModel
        interfaces = (relay.Node, )

class WhiteCardConnection(relay.Connection):
    class Meta:
        node = WhiteCard
