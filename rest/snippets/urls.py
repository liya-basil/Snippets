
from snippets.views import SnippetModelViewset
from snippets import views
from django.urls import path


urlpatterns = [

   path("snippet/",SnippetModelViewset.as_view({'get': 'list', 'post':'create'}),name="snippet"),
   path("snippet/<int:pk>/",SnippetModelViewset.as_view({'get': 'retrieve','delete':'destroy'}),name="snippet-detail"),

   path("snippets/",views.snippet_list),
   path("snippets/<int:pk>/",views.snippet_detail),


]