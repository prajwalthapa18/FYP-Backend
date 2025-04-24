from django.shortcuts import render
from django.http import JsonResponse

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def chart_data(request):
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May"],
        "values": [10, 15, 8, 12, 7]
    }
    return JsonResponse(data)
