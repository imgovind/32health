from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from claims.models import Claims
from claims.serializers import ClaimsSerializer
from claims.helpers import ConvertRequestToModel

# Create your views here.

@csrf_exempt
def claimsApi(request, id=0):
    if request.method == 'GET':
        claims = Claims.objects.all()
        claims_serializer = ClaimsSerializer(claims, many=True)
        return JsonResponse(claims_serializer.data, safe=False)
    elif request.method == 'POST':
        claims_json_data = JSONParser().parse(request)
        claims_data = ConvertRequestToModel(claims_json_data)
        claims_serializer = ClaimsSerializer(data=claims_data)
        if claims_serializer.is_valid():
            claims_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Couldn't Add", safe=False)
    else:
        return JsonResponse("Unsupported Operation", safe=False)
