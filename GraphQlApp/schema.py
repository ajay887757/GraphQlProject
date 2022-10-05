from email.policy import default
from tokenize import String
import graphene
from graphene_django import DjangoObjectType

from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model=Book
        field="__all__"


class Query(graphene.ObjectType):
    all_books=graphene.List(BookType)

    def resolve_all_books(root,info,*args,**kwargs):
        return Book.objects.all()
        



schema = graphene.Schema(query=Query)
