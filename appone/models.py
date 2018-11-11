from django.db import models

# Create your models here.

class Topic(models.Model):
    topicName = models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.topicName

class Webpage(models.Model):
    topic = models.ForeignKey('Topic',on_delete=models.CASCADE)
    webpageName = models.CharField(max_length=250,unique=True)
    webpageUrl = models.URLField()

    def __str__(self):
        return self.webpageName

class AccessRecord(models.Model):
    webpage = models.ForeignKey('Webpage',on_delete=models.CASCADE)
    accessedDate = models.DateField()

    def __str__(self):
        return str(self.accessedDate)