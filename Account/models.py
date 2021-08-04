from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=120)
    
    
    def __str__(self):
        return self.city_name

class Sex(models.Model):
    title = models.CharField(max_length=120)
    
    def __str__(self):
        return self.title


class ExtendedUser(models.Model):
    joined_date = models.DateTimeField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="images/", null=True)
    birthdate = models.DateField(null=True)

    def __str__(self):
        return str(self.user)
    