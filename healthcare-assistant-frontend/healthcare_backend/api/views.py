from django.http import JsonResponse

def get_symptoms(request):
    return JsonResponse({"message": "API is working!"})
