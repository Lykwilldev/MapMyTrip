from django.db import models

# Create your models here.


class Profile(models.Model): # Will be replaced with django's user model, serves no purpose now
    name = models.CharField(max_length=15)
    bio = models.CharField(max_length=2000)
    location = models.CharField(max_length=15)
    countries = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    #profile_picture = models.ImageField(upload_to='media/profile_pics', default='profile.jpg')
    #profile picture doesn't load, will figure out by the final deadline
    favorite_memory = models.CharField(max_length=50)

class Highlight(models.Model):
    country = models.CharField(max_length=50) 
    created_by= models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.CharField(max_length=50) 
    body = models.CharField(max_length=50) 
    date= models.DateField()

class Photo(models.Model):
    url= models.CharField()
    caption= models.CharField(max_length=50)
    included_in = models.ForeignKey(Highlight, on_delete=models.CASCADE)


class Comment(models.Model):
    body= models.CharField(max_length=150)
    made_by= models.ForeignKey(Profile, on_delete=models.CASCADE)
    in_highlight= models.ForeignKey(Highlight, on_delete=models.CASCADE)
    timestamp=models.DateField()

    