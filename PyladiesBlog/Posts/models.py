from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=30)
    date_created=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    slug =models.SlugField(max_length=120,unique=True,null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save (self,*args,**kwargs):
        if not self.slug:
            self.slug =slugify(self.title[:100] + str(now()))

        super(self,Post).save(*args,**kwargs)

    def __str__(self):
        return self.title