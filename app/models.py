from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    # fields for MyModel
    name = models.CharField(max_length=500)

class MyFile(models.Model):
    my_model = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')