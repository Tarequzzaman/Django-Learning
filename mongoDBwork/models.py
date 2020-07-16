from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.IntegerField()
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        managed = True
        db_table = 'posts'