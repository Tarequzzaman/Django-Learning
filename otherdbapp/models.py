from django.db import models
import uuid
# Create your models here.

class TimeStamField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class  Users(TimeStamField):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, blank=True,null=True)
    last_name = models.CharField(max_length=100,  blank=True,null=True)
    phone = models.CharField(max_length= 40)
    email = models.CharField(max_length=100, blank= False, null = False)
    class Meta:
        managed = True
        db_table = 'users'