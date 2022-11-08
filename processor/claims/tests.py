from django.test import TestCase
from claims.helpers.requestHelper import ValidateRequest

# Create your tests here.

class RequestHelperTests(TestCase):
    def validate_request_fails_on_null(TestCase):
        claims_json_data = None
        output = ValidateRequest(claims_json_data)
        self.assertIs(output, None)