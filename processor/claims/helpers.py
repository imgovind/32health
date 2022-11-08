import datetime

def ConvertRequestToModel(claims_json_data):
    # ServiceDate
    if "ServiceDate" in claims_json_data:
        dt = claims_json_data["ServiceDate"].split(' ')[0].split('/')
        ServiceDate = datetime.datetime(int('20' + dt[2]), int(dt[0]), int(dt[1]))
    else:
        return None

    # SubmittedProcedure
    if "SubmittedProcedure" in claims_json_data:
        SubmittedProcedure = claims_json_data["SubmittedProcedure"]
    else:
        return None

    # Quandrant
    if "Quadrant" in claims_json_data:
        Quadrant = claims_json_data["Quadrant"]
    else:
        Quadrant = None

    # PlanGroupNumber
    if "PlanGroupNumber" in claims_json_data:
        PlanGroupNumber = claims_json_data["PlanGroupNumber"]
    else:
        return None

    # SubscriberNumber
    if "SubscriberNumber" in claims_json_data:
        SubscriberNumber = claims_json_data["SubscriberNumber"]
    else:
        return None

    # ProviderNPI
    if "ProviderNPI" in claims_json_data:
        ProviderNPI = claims_json_data["ProviderNPI"]
    else:
        return None

    # ProviderFees
    if "ProviderFees" in claims_json_data:
        ProviderFees = int(float(claims_json_data["ProviderFees"].split("$")[1]) * 100)
    else:
        return None

    # AllowedFees
    if "AllowedFees" in claims_json_data:
        AllowedFees = int(float(claims_json_data["AllowedFees"].split("$")[1]) * 100)
    else:
        return None

    #MemberCoinsurance
    if "MemberCoinsurance" in claims_json_data:
        MemberCoinsurance = int(float(claims_json_data["MemberCoinsurance"].split("$")[1]) * 100)
    else:
        return None

    #MemberCopay
    if "MemberCopay" in claims_json_data:
        MemberCopay = int(float(claims_json_data["MemberCopay"].split("$")[1]) * 100)
    else:
        return None

    NetFee = ProviderFees + MemberCoinsurance + MemberCopay - AllowedFees

    claims_data = {}
    claims_data['ServiceDate'] = ServiceDate
    claims_data["SubmittedProcedure"] = SubmittedProcedure
    claims_data["Quadrant"] = Quadrant
    claims_data["PlanGroupNumber"] = PlanGroupNumber
    claims_data["SubscriberNumber"] = SubscriberNumber
    claims_data["ProviderNPI"] = ProviderNPI
    claims_data["ProviderFees"] = ProviderFees
    claims_data["AllowedFees"] = AllowedFees
    claims_data["MemberCoinsurance"] = MemberCoinsurance
    claims_data["MemberCopay"] = MemberCopay
    claims_data["NetFee"] = NetFee

    return claims_data