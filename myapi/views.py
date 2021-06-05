from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import  BookSerializer
from .serializers import AuthorSerializer
from .models import Book
from .models import Author
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



class BookViewSet (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet (viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @api_view(["GET"])
    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def welcome(request):
        content = {"message": "Welcome a mi libreria"}
        return JsonResponse(content)