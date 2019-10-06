from django.urls import path, include
from .views import home, noticia,listar_blogs

urlpatterns = [
    path('', home,name='home'),
    path('blog/<int:id>',noticia,name='noticias'),
    path('',listar_blogs,name='listar_blogs'),
    ]  