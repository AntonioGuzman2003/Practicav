from django.urls import path
from server.views.views_post import getPosts

urlpatterns = [
    path('',getPosts.as_view(),name="getPosts"),
    
]
