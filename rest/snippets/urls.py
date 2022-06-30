
from django.contrib import admin
from django.urls import path

from snippets.views import SnippetModelViewset

urlpatterns = [

   path("snippet/",SnippetModelViewset.as_view({'get': 'list'}),name="snippet")


]