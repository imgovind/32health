import datetime

def ValidateRequest(claims_json_data):
    # Null check
    if claims_json_data == None:
        return None

    # ServiceDate
    if "ServiceDate" not in claims_json_data:
        return None
    dt = claims_json_data["ServiceDate"].split(' ')[0].split('/')
    ServiceDate = datetime.datetime(int('20' + dt[2]), int(dt[0]), int(dt[1]))

    # SubmittedProcedure
    if "SubmittedProcedure" not in claims_json_data:
        return None
    SubmittedProcedure = claims_json_data["SubmittedProcedure"]

    # Check if the submitted procedure starts with D
    if SubmittedProcedure.split[0] != 'D':
        return None

    # Quandrant
    Quadrant = None
    if "Quadrant" in claims_json_data:
        Quadrant = claims_json_data["Quadrant"]

    # PlanGroupNumber
    if "PlanGroupNumber" not in claims_json_data:
        return None
    PlanGroupNumber = claims_json_data["PlanGroupNumber"]

    # SubscriberNumber
    if "SubscriberNumber" not in claims_json_data:
        return None
    SubscriberNumber = claims_json_data["SubscriberNumber"]

    # ProviderNPI
    if "ProviderNPI" not in claims_json_data:
        return None
    ProviderNPI = claims_json_data["ProviderNPI"]

    # Check if provider NPI is of length 10
    if len(ProviderNPI) != 10:
        return None

    # ProviderFees
    if "ProviderFees" not in claims_json_data:
        return None
    ProviderFees = int(float(claims_json_data["ProviderFees"].split("$")[1]) * 100)

    # AllowedFees
    if "AllowedFees" not in claims_json_data:
        return None
    AllowedFees = int(float(claims_json_data["AllowedFees"].split("$")[1]) * 100)

    #MemberCoinsurance
    if "MemberCoinsurance" not in claims_json_data:
        return None
    MemberCoinsurance = int(float(claims_json_data["MemberCoinsurance"].split("$")[1]) * 100)

    #MemberCopay
    if "MemberCopay" not in claims_json_data:
        return None
    MemberCopay = int(float(claims_json_data["MemberCopay"].split("$")[1]) * 100)

    # Calculate NetFee
    NetFee = ProviderFees + MemberCoinsurance + MemberCopay - AllowedFees

    claims_data = {
        "ServiceDate" : ServiceDate,
        "SubmittedProcedure" : SubmittedProcedure,
        "Quadrant" : Quadrant,
        "PlanGroupNumber" : PlanGroupNumber,
        "SubscriberNumber" : SubscriberNumber,
        "ProviderNPI" : ProviderNPI,
        "ProviderFees" : ProviderFees,
        "AllowedFees" : AllowedFees,
        "MemberCoinsurance" : MemberCoinsurance,
        "MemberCopay" : MemberCopay,
        "NetFee" : NetFee,
    }

    return claims_data