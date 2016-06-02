from django.db import models
from django.utils import timezone

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=12)
    email = models.EmailField()
    fbpagelink = models.URLField()
    address = models.TextField()
    meetuplink = models.URLField()
    polynteer = models.BooleanField()
    eventshosted = models.SmallIntegerField()
    eventshostedname = models.CharField(max_length=200)
    ohb = models.BooleanField()
    ohbcontributions = models.SmallIntegerField()
    launchteam = models.BooleanField()
    launchteamcontributions = models.SmallIntegerField()
    fbgroupmember = models.BooleanField()
    donationtotalammount = models.SmallIntegerField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
