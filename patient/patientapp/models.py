from django.db import models

# Create your models here.
class patient(models.Model):
    cNAME = models.CharField(max_length=20, null=False)
    cID = models.CharField(max_length=20, null=False)
    cGENDER = models.CharField(max_length=10, null=False)
    cAGE = models.CharField(max_length=10, blank=True, default='')
    cWHERE = models.CharField(max_length=100, null=False)
    cPAINSITE = models.CharField(max_length=100, null=False)
    cWHEN = models.CharField(max_length=100, null=False)
    cHOW = models.CharField(max_length=100, null=False)
    cPROVOCATION = models.CharField(max_length=100, blank=True, default='')
    cPAINLEVEL = models.CharField(max_length=100, null=False)
    cPI = models.CharField(max_length=500, null=False)
    def __str__(self):
        return self.cNAME

