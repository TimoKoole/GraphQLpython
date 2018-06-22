import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Regeling as RegelingModel
from models import RegelingWaardes as RegelingWaardesModel

class Regeling(MongoengineObjectType):
    class Meta:
        model = RegelingModel
        interfaces = (Node,)

class RegelingWaardes(MongoengineObjectType):
    class Meta:
        model = RegelingWaardesModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    regelingen = MongoengineConnectionField(Regeling)

schema = graphene.Schema(query=Query, types=[Regeling, RegelingWaardes])
