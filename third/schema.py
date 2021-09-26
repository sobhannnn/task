import graphene
from graphene_django.types import DjangoObjectType
from accounts.models import MyUser

class MyUserType(DjangoObjectType):
    class Meta:
        model = MyUser
        fields = ("__all__")
class Query(graphene.ObjectType):
    all_users = graphene.List(MyUserType)

    def resolve_all_users(root, info):
        return MyUser.objects.all()

schema = graphene.Schema(query=Query)