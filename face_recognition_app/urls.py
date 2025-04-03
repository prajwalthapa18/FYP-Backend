from django.urls import path
from .views import save_detected_user, get_gender_count

urlpatterns = [
    path('save_user/', save_detected_user, name='save_user'),
    path('gender_count/', get_gender_count, name='gender_count'),
]
