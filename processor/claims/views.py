from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from claims.models import Claims
from claims.services.claims_service import process_claim

# Create your views here.

@csrf_exempt
def claimsApi(request, id=0):
    if request.method == 'GET':
        claims = Claims.objects.all()
        claims_serializer = ClaimsSerializer(claims, many=True)
        return JsonResponse(claims_serializer.data, safe=False)
    elif request.method == 'POST':
        claims_json_data = JSONParser().parse(request)

        # Request could not be processed
        if not process_claim(claims_json_data):
            return JsonResponse({'status': False, 'message':'Request could not be processed'}, status=400, safe=False)

        # Request was successfully processed
        return JsonResponse({'status': True, 'message':'Added successfully'}, status=200, safe=False)
    else:
        # Unsupported operation
        return JsonResponse({'status': False, 'message':'Unsupported Operation'}, status=400, safe=False)
