from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Item(models.Model):
    title=  models.CharField(max_length= 250, blank= True)
    price= models.FloatField()
    order= models.BooleanField(default= False)

    class Meta:
        verbose_name= _('Item')
        verbose_name_plural= _('Items')
            
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super.save(*args, **kwargs)
        if self.order== True:
            Updated.objects.create(self)

class Updated(models.Model):
    item= models.ForeignKey(Item, on_delete= models.CASCADE, related_name='updated_item')

    class Meta:
        abstract= True


class OrderedItem(Updated):
    ordered= models.BooleanField(default=True)
    
    class Meta:
        verbose_name= _('OrderedItem')
        verbose_name_plural= _('OrderedItems')

    def __str__(self):
        return self.item.title & self.item.price

class Cart(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items= models.ManyToManyField(OrderedItem)
    placement_time= models.DateTimeField(auto_now_add= True)
    order_time= models.DateTimeField()
    class Meta:
        ordering=["placement_time"]
        
    def __str__(self):
        return self.user.username

# Create your models here.
