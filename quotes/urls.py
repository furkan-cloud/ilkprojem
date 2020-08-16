from django.urls import path, re_path
from . import views

#(?P<id>\d+)/


urlpatterns = [
    path('', views.index, name='quotes'),
    path('create', views.create, name= 'create'),
    path(r'<slug>/', views.detail, name= 'detail'),
    path('search', views.search, name= 'search'),
    path(r'<slug>/update', views.update, name= 'update'),
    path(r'<slug>/delete', views.delete, name= 'delete'),
]