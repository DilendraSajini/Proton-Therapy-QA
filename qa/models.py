from django.db import models

class PDDSession(models.Model):
    adate = models.DateTimeField()
    machine = models.CharField(max_length=100)
    operator1 = models.CharField(max_length=100, blank=True)

class PDDResult(models.Model):
    session = models.ForeignKey(PDDSession,on_delete=models.CASCADE)
    energy = models.FloatField()
    p80 = models.FloatField(default=0)
    p90 = models.FloatField(default=0)
    ptpr = models.FloatField(default=0)
