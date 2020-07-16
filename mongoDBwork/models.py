from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(max_length=400,blank=False, default='')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        managed = True
        db_table = 'posts'