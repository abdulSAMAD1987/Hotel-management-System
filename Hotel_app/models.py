from django.db import models
from django.contrib.auth.models import User, AbstractUser


# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=20, null=True, blank=True)
#
#     def __str__(self):
#         return self.username


class Facilities(models.Model):
    facility = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.facility


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    facilities = models.ManyToManyField(Facilities)
    descriptions = models.TextField()
    images = models.ImageField(upload_to="media")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.hotel.name
