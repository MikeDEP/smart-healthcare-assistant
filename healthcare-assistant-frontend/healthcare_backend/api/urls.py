from django.urls import path
from .views import get_symptoms

urlpatterns = [
    path('symptoms/', get_symptoms),
]
