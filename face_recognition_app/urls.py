from django.urls import path
from .views import save_detected_user, get_gender_count, get_last_user_id

urlpatterns = [
    path('save_user/', save_detected_user, name='save_user'),
    path('gender_count/', get_gender_count, name='gender_count'),
    path('save_user_last_id/', get_last_user_id, name='get_last_user_id'),

]
