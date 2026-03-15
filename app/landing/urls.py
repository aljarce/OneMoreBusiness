from django.urls import path
from .views import questionnaire_view

urlpatterns = [
    path('', questionnaire_view, name='questionnaire'),
]
