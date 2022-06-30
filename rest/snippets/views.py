from django.shortcuts import render
from rest_framework import viewsets

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# Create your views here.
class SnippetModelViewset(viewsets.ModelViewSet):
    queryset= Snippet.objects.all()
    serializer_class= SnippetSerializer