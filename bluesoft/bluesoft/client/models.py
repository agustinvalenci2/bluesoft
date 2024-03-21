from django.db import models

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city_of_origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
