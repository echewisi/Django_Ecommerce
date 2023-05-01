from django.db import models
from django.conf import settings

class Item(models.Model):
    title=  models.CharField(max_length= 250, blank= True)
    price= models.FloatField()
    
    def __str__(self):
        return self.title

class OrderedItem(models.Model):
    item= models.ForeignKey(Item, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return self.item.title & self.item.price

class Cart(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items= models.ManyToManyField(OrderedItem)
    ordered= models.BooleanField(default= False)
    placement_time= models.DateTimeField(auto_now_add= True)
    order_time= models.DateTimeField()
    def __str__(self):
        return self.user.username

# Create your models here.
