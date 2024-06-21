from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('me/', views.MeView.as_view(), name='me'),
    path('create/', views.PostCreateView.as_view(), name='create'),
]
