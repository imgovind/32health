import datetime
from claims.constants import ClaimsFields

def validate_request(claims_json_data):
    # Null check
    if claims_json_data == None:
        return None

    # ServiceDate
    if ClaimsFields.ServiceDate not in claims_json_data:
        return None
    dt = claims_json_data[ClaimsFields.ServiceDate].split(' ')[0].split('/')
    ServiceDate = datetime.datetime(int('20' + dt[2]), int(dt[0]), int(dt[1]))

    # SubmittedProcedure
    if ClaimsFields.SubmittedProcedure not in claims_json_data:
        return None
    SubmittedProcedure = claims_json_data[ClaimsFields.SubmittedProcedure]

    # Check if the submitted procedure starts with D
    if SubmittedProcedure[0] != 'D':
        return None

    # Quandrant
    Quadrant = None
    if ClaimsFields.Quadrant in claims_json_data:
        Quadrant = claims_json_data[ClaimsFields.Quadrant]

    # PlanGroupNumber
    if ClaimsFields.PlanGroupNumber not in claims_json_data:
        return None
    PlanGroupNumber = claims_json_data[ClaimsFields.PlanGroupNumber]

    # SubscriberNumber
    if ClaimsFields.SubscriberNumber not in claims_json_data:
        return None
    SubscriberNumber = claims_json_data[ClaimsFields.SubscriberNumber]

    # ProviderNPI
    if ClaimsFields.ProviderNPI not in claims_json_data:
        return None
    ProviderNPI = claims_json_data[ClaimsFields.ProviderNPI]

    # Check if provider NPI is of length 10
    if len(ProviderNPI) != 10:
        return None

    # ProviderFees
    if ClaimsFields.ProviderFees not in claims_json_data:
        return None
    ProviderFees = int(float(claims_json_data[ClaimsFields.ProviderFees].split("$")[1]) * 100)

    # AllowedFees
    if ClaimsFields.AllowedFees not in claims_json_data:
        return None
    AllowedFees = int(float(claims_json_data[ClaimsFields.AllowedFees].split("$")[1]) * 100)

    #MemberCoinsurance
    if ClaimsFields.MemberCoinsurance not in claims_json_data:
        return None
    MemberCoinsurance = int(float(claims_json_data[ClaimsFields.MemberCoinsurance].split("$")[1]) * 100)

    #MemberCopay
    if ClaimsFields.MemberCopay not in claims_json_data:
        return None
    MemberCopay = int(float(claims_json_data[ClaimsFields.MemberCopay].split("$")[1]) * 100)


    claims_data = {
        ClaimsFields.ServiceDate : ServiceDate,
        ClaimsFields.SubmittedProcedure : SubmittedProcedure,
        ClaimsFields.Quadrant : Quadrant,
        ClaimsFields.PlanGroupNumber : PlanGroupNumber,
        ClaimsFields.SubscriberNumber : SubscriberNumber,
        ClaimsFields.ProviderNPI : ProviderNPI,
        ClaimsFields.ProviderFees : ProviderFees,
        ClaimsFields.AllowedFees : AllowedFees,
        ClaimsFields.MemberCoinsurance : MemberCoinsurance,
        ClaimsFields.MemberCopay : MemberCopay
    }

    return claims_data