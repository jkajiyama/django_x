from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('my', views.MyProfileView.as_view(), name='my'),
    path('my/update', views.ProfileUpdateView.as_view(), name='update'),
]
