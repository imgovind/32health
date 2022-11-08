from claims.serializers import ClaimsSerializer
from claims.services.events_service import sendClaimProcessedEvent
from claims.helpers.request_helper import ValidateRequest
from claims.constants import ClaimsFields

def processClaim(claims_json_data):
    claims_data = ValidateRequest(claims_json_data)
    # print(claims_data)
    NetFee = calculateNetFees(claims_data)
    claims_data[ClaimsFields.NetFee] = NetFee

    claims_serializer = ClaimsSerializer(data=claims_data)

    if(claims_serializer.is_valid() != True):
        return False

    # Saving to the Database
    claims_serializer.save()

    # Over here what I would do is use RabbitMQ or Kafka
    # Send a message to a queue to which the payment service has subscribed to
    # Using this Async model trigger events downstream and chain processes
    # If the processing required a long chain of tasks, then use a library like luigi to chain them nicer
    # could also use a service bus to talk to it but keep it simple
    sendClaimProcessedEvent(claims_data)

    return True

def calculateNetFees(claims_data):
    required_fields = [ClaimsFields.ProviderFees, ClaimsFields.AllowedFees, ClaimsFields.MemberCoinsurance, ClaimsFields.MemberCopay]
    all_fields = list(claims_data.keys())


    print(required_fields)
    print(all_fields)
    
    if not any(field in required_fields for field in all_fields):
        return None

    # Calculate NetFee
    NetFee = claims_data[ClaimsFields.ProviderFees] + \
         claims_data[ClaimsFields.MemberCoinsurance] + \
            claims_data[ClaimsFields.MemberCopay] - \
                claims_data[ClaimsFields.AllowedFees]

    return NetFee