
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100,default="write the title")
    author = models.CharField(max_length=30,default="write the author name")
    introduction = models.TextField(max_length=1000,default="what is the intro")
    description = models.TextField(max_length=7000,default="provide the dessc")
    slug = models.CharField(max_length=200,default="what is the slug")
    tumbnail = models.ImageField(upload_to='images/',) 
    category = models.CharField(max_length=30,default="tech")
    release_date = models.DateField(default=date.today)
    

    def __str__(self) -> str:
        return self.title

class BlogComment(models.Model):
    id = models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    Date = models.DateField(default=date.today)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
    


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=3000)
    Date = models.DateField(default=date.today)
    

    def __str__(self) -> str:
        return self.fullname
     