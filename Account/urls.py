from django.urls import path, include
from .api import RegisterApi
urlpatterns = [
      path('api/login/', RegisterApi.as_view()),
]