from claims.serializers import ClaimsSerializer
from claims.helpers import ValidateRequest
from claims.services.eventService import sendClaimProcessedEvent
from claims.constants import ClaimsFields

def processClaim(claims_json_data):
    claims_data = ValidateRequest(claims_json_data)
    claims_serializer = ClaimsSerializer(data=claims_data)

    if(claims_serializer.is_valid() != True):
        return False

    claims_data[ClaimsFields.NetFee] = calculateNetFees(claims_data)

    claims_serializer.save()
    sendClaimProcessedEvent(claims_data)
    return True

def calculateNetFees(claims_data):
    required_fields = [ClaimsFields.ProviderFees, ClaimsFields.MemberCoinsurance, ClaimsFields.MemberCopay, ClaimsFields.AllowedFees]
    all_fields = list(claims_data.keys())
    
    if required_fields not in all_fields:
        return None

    # Calculate NetFee
    NetFee = claims_data[ClaimsFields.ProviderFees] + claims_data[ClaimsFields.MemberCoinsurance] + claims_data[ClaimsFields.MemberCopay] - claims_data[ClaimsFields.AllowedFees]

    return NetFee