from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from claims.models import Claims
from claims.services.claimsService import processClaim

# Create your views here.

@csrf_exempt
def claimsApi(request, id=0):
    if request.method == 'GET':
        claims = Claims.objects.all()
        claims_serializer = ClaimsSerializer(claims, many=True)
        return JsonResponse(claims_serializer.data, safe=False)
    elif request.method == 'POST':
        claims_json_data = JSONParser().parse(request)

        if processClaim(claims_json_data):
            return JsonResponse({'status':'false','message':'Added successfully'}, status=200, safe=False)

            # Over here what I would do is use RabbitMQ or Kafka
            # Send a message to a queue to which the payment service has subscribed to
            # Using this Async model trigger events downstream and chain processes
            # If the processing required a long chain of tasks, then use a library like luigi to chain them nicer
            # could also use a service bus to talk to it but keep it simple

        else:
            return JsonResponse({'status':'false','message':'Bad Request'}, status=400, safe=False)
    else:
        return JsonResponse({'status':'false','message':'Unsupported Operation'}, status=400, safe=False)
