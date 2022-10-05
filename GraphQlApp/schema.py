from dataclasses import fields
from pyexpat import model
import graphene

from .models import Book

class BookType(graphene.ObjectType):
    class Meta:
        model=Book,
        fields="__all__"


class Query(graphene.ObjectType):
    all_books=graphene.List(BookType)



schema = graphene.Schema(query=Book)
