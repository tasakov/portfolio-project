from django.db import models

class Job(models.Model):
    #whenever someone uploads an image-where do we want to save it?
    #inside a media folder there will be an images folder
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
