from django.urls import path

from . import views


app_name = 'sports'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.sports_list, name='list'),
    path('create/', views.sports_create, name='create'),
    path('detail/<int:pk>/', views.sports_detail, name='detail'),
    path('update/<int:pk>/', views.sports_update, name='update'),
    path('delete/<int:pk>/', views.sports_delete, name='delete'),
]
