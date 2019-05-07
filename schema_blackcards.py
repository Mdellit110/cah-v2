import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.models import *

class BlackCard(SQLAlchemyObjectType):
    class Meta:
        model = BlackCardModel
        interfaces = (relay.Node, )

class BlackCardConnection(relay.Connection):
    class Meta:
        node = BlackCard
