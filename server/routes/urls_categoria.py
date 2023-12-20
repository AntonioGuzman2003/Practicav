from django.urls import path
from server.views.views_categoria import getCategorias

urlpatterns = [
    path('',getCategorias.as_view(),name="get_categorias"),
    
]
