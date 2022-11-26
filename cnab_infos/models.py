from django.db import models
import uuid

# Create your models here.

class Operations(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type= models.CharField(max_length=1)
    date= models.CharField(max_length=10)
    value= models.FloatField()
    cpf= models.CharField(max_length=11)
    card= models.CharField(max_length=12)
    hour= models.CharField(max_length=8)
    store_owner= models.CharField(max_length=15)
    store_name= models.CharField(max_length=20)



class File(models.Model):
    File = models.FileField()
    date= models.DateTimeField(auto_now_add=True )

 