from django.test import TestCase
from claims.helpers.request_helper import validate_request
from claims.services.claims_service import calculate_net_fees, process_claim


class ClaimsServiceTest(TestCase):
    def setUp(self):
        self.claims_json_data = {
            "ServiceDate": "3/28/18 0:00",
            "Quadrant": "UH",
            "SubmittedProcedure": "D0210",
            "PlanGroupNumber": "GRP-1000",
            "SubscriberNumber": "3730189502",
            "ProviderNPI": "1497775530",
            "ProviderFees": "$108.00",
            "AllowedFees": "$108.00",
            "MemberCoinsurance": "$0.00",
            "MemberCopay": "$0.0"
        }

    def test_calculate_net_fees_succeeds(self):
        claims_data = validate_request(self.claims_json_data)
        netfees = calculate_net_fees(claims_data)
        self.assertEquals(netfees, 0)

    def test_calculate_net_fees_succeeds_2(self):
        self.claims_json_data["MemberCoinsurance"] = "$50.00"
        claims_data = validate_request(self.claims_json_data)
        netfees = calculate_net_fees(claims_data)
        self.assertEquals(netfees, 5000)

    def test_process_claim_fails_missing_fields(self):
        del self.claims_json_data['ProviderNPI']
        status = process_claim(self.claims_json_data)
        self.assertEquals(status, False)

    def test_process_claim_fails_with_invalid_providerNPI(self):
        self.claims_json_data['ProviderNPI'] = '123456789'
        status = process_claim(self.claims_json_data)
        self.assertEquals(status, False)

    def test_process_claim_fails_with_invalid_submitted_procedure(self):
        self.claims_json_data['SubmittedProcedure'] = '0210'
        status = process_claim(self.claims_json_data)
        self.assertEquals(status, False)

    def test_process_claim_succeeds(self):
        status = process_claim(self.claims_json_data)
        self.assertNotEquals(status, False)
