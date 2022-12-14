from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from claims.serializers import ClaimsSerializer

from claims.models import Claims
from claims.services.claims_service import process_claim

# Create your views here.

@csrf_exempt
def claimsApi(request, id=0):
    if request.method == 'GET':
        claims = Claims.objects.all()
        claims_serializer = ClaimsSerializer(claims, many=True)
        return JsonResponse({'status': True, 'message': 'Success', 'data': claims_serializer.data }, status=200, safe=False)
    elif request.method == 'POST':
        claims_json_data = JSONParser().parse(request)

        # Request could not be processed
        claim = process_claim(claims_json_data)
        if not claim:
            return JsonResponse({'status': False, 'message':'Request could not be processed'}, status=400, safe=False)

        # Request was successfully processed
        return JsonResponse({'status': True, 'message':'Success', 'data': claim}, status=200, safe=False)
    else:
        # Unsupported operation
        return JsonResponse({'status': False, 'message':'Unsupported Operation'}, status=400, safe=False)
