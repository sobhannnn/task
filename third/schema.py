import graphene
from graphene_django.types import DjangoObjectType
from accounts.models import MyUser
import graphql_jwt

class MyUserType(DjangoObjectType):
    class Meta:
        model = MyUser
        fields = ("__all__")
class Query(graphene.ObjectType):
    all_users = graphene.List(MyUserType)

    def resolve_all_users(root, info):
        return MyUser.objects.all()



class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)