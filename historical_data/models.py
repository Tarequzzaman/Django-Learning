from django.db import models
from datetime import datetime
from django.utils import timezone
import uuid

# Create your models here.

from django.utils.translation import ugettext as translate
from django.utils.timezone import now






class TimeStamField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class PriceHistory(TimeStamField):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.DecimalField(max_digits=7, decimal_places=3)

    class Meta:
        managed = True
        db_table = 'price_history'
    def __unicode__(self):
            return self.id
    def __str__(self):
        return '{}, {}, {}'.format(self.id, self.price, self.volume)



class  Users(TimeStamField):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, blank=True,null=True)
    last_name = models.CharField(max_length=100,  blank=True,null=True)
    phone = models.CharField(max_length= 40)
    email = models.CharField(max_length=100, blank= False, null = False)
    class Meta:
        managed = True
        db_table = 'users'







