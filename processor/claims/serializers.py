from rest_framework import serializers
from claims.models import Claims

class ClaimsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Claims
        fields=('ClaimsId',
                'ServiceDate',
                'SubmittedProcedure',
                'Quadrant',
                'PlanGroupNumber',
                'SubscriberNumber',
                'ProviderNPI',
                'ProviderFees',
                'AllowedFees',
                'MemberCoinsurance',
                'MemberCopay',
                'NetFee')