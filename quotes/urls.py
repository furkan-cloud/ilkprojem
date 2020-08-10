from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='quotes'),
    path('<int:quote_id>', views.detail, name= 'detail'),
    path('search', views.search, name= 'search'),
    path('create', views.create, name= 'create'),
    path('update', views.update, name= 'update'),
    path('<int:quote_id>/delete', views.delete, name= 'delete'),
]