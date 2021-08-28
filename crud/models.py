from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + " " + self.name