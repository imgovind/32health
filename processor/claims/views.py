from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from claims.models import Claims
from claims.serializers import ClaimsSerializer
from claims.helpers import ValidateRequest

# Create your views here.

@csrf_exempt
def claimsApi(request, id=0):
    if request.method == 'GET':
        claims = Claims.objects.all()
        claims_serializer = ClaimsSerializer(claims, many=True)
        return JsonResponse(claims_serializer.data, safe=False)
    elif request.method == 'POST':
        claims_json_data = JSONParser().parse(request)
        claims_data = ValidateRequest(claims_json_data)
        claims_serializer = ClaimsSerializer(data=claims_data)
        if claims_serializer.is_valid():
            claims_serializer.save()
            return JsonResponse("Added Successfully", safe=False)

            # Over here what I would do is use RabbitMQ or Kafka
            # Send a message to a queue to which the payment service has subscribed to
            # Using this Async model to keep track of the downstream processes
            # could also use a service bus to talk to it but 

        else:
            return JsonResponse("Invalid Data", safe=False)
    else:
        return JsonResponse("Unsupported Operation", safe=False)
