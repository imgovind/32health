from django.test import TestCase
from claims.helpers.request_helper import ValidateRequest

class TestRequestHelper(TestCase):
    def test_request_helper_fails_on_null(self):
        claims_json_data = None
        output = ValidateRequest(claims_json_data)
        self.assertEqual(output, None)