from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_page, name='map'),
    path('<str:name>/', views.post_list_by_location, name='posts_by_location'),
]
