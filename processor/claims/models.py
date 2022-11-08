from django.db import models

# Create your models here.
class Claims(models.Model):
    ClaimsId = models.AutoField(primary_key=True)
    ServiceDate = models.DateTimeField()
    SubmittedProcedure = models.CharField(max_length=10)
    Quadrant = models.CharField(max_length=2, null=True)
    PlanGroupNumber = models.CharField(max_length=20)
    SubscriberNumber = models.CharField(max_length=20)
    ProviderNPI = models.CharField(max_length=20)
    ProviderFees = models.IntegerField()
    AllowedFees = models.IntegerField()
    MemberCoinsurance = models.IntegerField()
    MemberCopay  = models.IntegerField() 
    NetFee = models.IntegerField()
