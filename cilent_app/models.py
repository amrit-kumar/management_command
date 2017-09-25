from django.db import models
# import JSONField


# Create your models here.
class Api(models.Model):
    api=models.CharField(max_length=500)