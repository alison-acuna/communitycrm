from django.db import models
from django.utils import timezone

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=200)
    meetupid = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=12)
    volunteer = models.NullBooleanField()
    host = models.SmallIntegerField()
    eventshostedname = models.CharField(max_length=200)
    ohb = models.NullBooleanField()
    ohbcontributions = models.SmallIntegerField()
    launchteam = models.NullBooleanField()
    launchteamcontributions = models.SmallIntegerField()
    fbgroupmember = models.NullBooleanField()
    fbpagelink = models.URLField()
    donationtotalammount = models.SmallIntegerField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def engagement_score(self):
        engagement_score = 0
        if self.volunteer:
            engagement_score += 1
        if self.ohb:
            engagement_score += 1
        if self.launchteam:
            engagement_score += 1
        if self.donationtotalammount > 0:
            engagement_score += 5
        engagement_score = engagement_score + self.host + self.ohbcontributions + self.launchteamcontributions
        return engagement_score
