from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person, Count
from .serializers import PersonSerializer, CountSerializer

@api_view(['GET'])
def gender_count(request):
    # Update count in the database
    Count.update_counts()
    count = Count.objects.first()
    serializer = CountSerializer(count)
    return Response(serializer.data)

@api_view(['POST'])
def add_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        Count.update_counts()  # Update count after adding a person
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
