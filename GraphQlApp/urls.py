# from django.conf.urls import url
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .schema import schema


# urlpatterns = [
#     # ...
#     path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
# ]

urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True,schema=schema)),
]