from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DetectedUser, GenderCount
import json

@csrf_exempt
def save_detected_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        gender = data.get('gender')

        if user_id and gender:
            # Save or update the detected user
            DetectedUser.objects.update_or_create(user_id=user_id, defaults={'gender': gender})

            # Update gender count
            gender_obj, created = GenderCount.objects.get_or_create(gender=gender)
            gender_obj.count += 1
            gender_obj.save()

            return JsonResponse({'message': 'User data saved successfully'}, status=201)

        return JsonResponse({'error': 'Invalid data'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=405)

def get_gender_count(request):
    male_count = GenderCount.objects.filter(gender="Male").first()
    female_count = GenderCount.objects.filter(gender="Female").first()

    return JsonResponse({
        'Male': male_count.count if male_count else 0,
        'Female': female_count.count if female_count else 0
    })
