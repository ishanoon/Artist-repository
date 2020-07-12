from django.urls import path
from . import views

urlpatterns = [
    path("",views.artist_directory, name="home"),
    path("profile/<str:pk>/", views.artist_profile,name="profile")
]
