from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import DetectedUser, GenderCount, Counter

@csrf_exempt
def save_detected_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    gender = request.POST.get("gender")
    image  = request.FILES.get("image")

    if not gender:
        return JsonResponse({"error": "Gender is required"}, status=400)

    user = DetectedUser.objects.create(gender=gender, image=image)

    gender_obj, _ = GenderCount.objects.get_or_create(gender=gender)
    gender_obj.count = DetectedUser.objects.filter(gender=gender).count()
    gender_obj.save()

    return JsonResponse({"message": "Saved", "user_id": user.id}, status=201)


    # Create user with the new ID
    DetectedUser.objects.create(
        user_id=counter.last_user_id,
        gender=gender,
        image=image
    )

    # Update gender count
    gender_obj, _ = GenderCount.objects.get_or_create(gender=gender)
    gender_obj.count += 1
    gender_obj.save()

    return JsonResponse({
        "message": "User data saved successfully",
        "user_id": counter.last_user_id
    }, status=201)

def get_gender_count(request):
    male = GenderCount.objects.filter(gender="Male").first()
    female = GenderCount.objects.filter(gender="Female").first()

    return JsonResponse({
        "Male": male.count if male else 0,
        "Female": female.count if female else 0,
    })

@csrf_exempt
def get_last_user_id(request):
    if request.method != "GET":
        return JsonResponse({"error": "Invalid request"}, status=405)
    
    counter = Counter.objects.first()
    return JsonResponse({
        "last_user_id": counter.last_user_id if counter else 0
    })