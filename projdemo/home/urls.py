from django.urls import path
from home.views import HomeView


urlpatterns = [
    path('hello/', HomeView.as_view(), name='hello'),
]