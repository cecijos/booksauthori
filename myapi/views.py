from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import  BookSerializer
from .serializers import AuthorSerializer
from .models import Book
from .models import Author


class BookViewSet (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet (viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer