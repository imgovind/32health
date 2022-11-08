from django.test import TestCase
from claims.helpers.request_helper import validate_request

class TestRequestHelper(TestCase):
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

    def test_request_helper_fails_on_null(self):
        self.claims_json_data = None
        output = validate_request(self.claims_json_data)
        self.assertEqual(output, None)

    def test_request_helper_fails_on_missing_required_fields(self):
        del self.claims_json_data['ProviderNPI']
        output = validate_request(self.claims_json_data)
        self.assertEqual(output, None)

    def test_request_helper_fails_on_invalid_providerNPI(self):
        self.claims_json_data['ProviderNPI'] = '123456789'
        output = validate_request(self.claims_json_data)
        self.assertEqual(output, None)   

    def test_request_helper_fails_on_invalid_submitted_procedure(self):
        self.claims_json_data['SubmittedProcedure'] = '0210'
        output = validate_request(self.claims_json_data)
        self.assertEqual(output, None)   

    def test_request_helper_succeeds_on_missing_optional_fields(self):
        del self.claims_json_data['Quadrant']
        output = validate_request(self.claims_json_data)
        self.assertNotEquals(output, None)
    
    def test_request_helper_succeeds_on_valid_fields(self):
        output = validate_request(self.claims_json_data)
        self.assertNotEquals(output, None)