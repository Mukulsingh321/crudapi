import email
from django.db import models

# Create your models here.

class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.name