from django.urls import path
from .views import gender_count, add_person

urlpatterns = [
    path('gender-count/', gender_count, name='gender_count'),
    path('add-person/', add_person, name='add_person'),
]
