from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.
#define modal of class
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.IntegerField()
    photo_main1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_main2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
