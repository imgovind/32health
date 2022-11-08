import asyncio
from claims.serializers import ClaimsSerializer
from claims.services.events_service import send_claim_processed_event
from claims.helpers.request_helper import validate_request
from claims.constants import ClaimsFields

def process_claim(claims_json_data):
    claims_data = validate_request(claims_json_data)

    # Invalid claims data
    if claims_data == None:
        return False

    # Calculate and set NetFees
    NetFee = calculate_net_fees(claims_data)
    claims_data[ClaimsFields.NetFee] = NetFee

    # Run serializer
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
    asyncio.run(send_claim_processed_event(claims_data))

    return claims_serializer.data

def calculate_net_fees(claims_data):
    required_fields = [ClaimsFields.ProviderFees, ClaimsFields.AllowedFees, ClaimsFields.MemberCoinsurance, ClaimsFields.MemberCopay]
    all_fields = list(claims_data.keys())

    if not any(field in required_fields for field in all_fields):
        return None

    # Calculate NetFee
    NetFee = claims_data[ClaimsFields.ProviderFees] + \
         claims_data[ClaimsFields.MemberCoinsurance] + \
            claims_data[ClaimsFields.MemberCopay] - \
                claims_data[ClaimsFields.AllowedFees]

    return NetFee