from email.policy import default
from tokenize import String
from turtle import title
import graphene
from graphene_django import DjangoObjectType

from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model=Book
        field="__all__"


class Query(graphene.ObjectType):
    all_books=graphene.List(BookType)
    all_books=graphene.List(BookType,data=graphene.String(),title_data=graphene.String())   # to getting Input From Query Set
    def resolve_all_books(root,info,data,title_data,*args,**kwargs,):
   
  
    # def resolve_all_books(root,info,*args,**kwargs,):
        return Book.objects.all()


#adding new entry using mutation on db   go throught to readme file
class TitleMutation(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        description=graphene.String()
    
    BookData=graphene.Field(BookType)
    
    @classmethod
    def mutate(cls,root,info,name,description):
        Books=Book(title=name,excerpt=description)
        Books.save()

        return TitleMutation(BookData=Books)


        
class Mutation(graphene.ObjectType):
    update_title=TitleMutation.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)
