
# from snippets.views import SnippetModelViewset
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

   # path("snippet/",SnippetModelViewset.as_view({'get': 'list', 'post':'create'}),name="snippet"),
   # path("snippet/<int:pk>/",SnippetModelViewset.as_view({'get': 'retrieve','delete':'destroy'}),name="snippet-detail"),

   path("snippets/",views.SnippetList.as_view()),
   path("snippets/<int:pk>/",views.SnippetDetail.as_view()),

# 
]
# ADDING OPTIONAL FORMAT SUFFIXES TO OUR URLS
urlpatterns = format_suffix_patterns(urlpatterns)

