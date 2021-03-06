from django.db import models

from django.contrib.auth.models import User


# Create your models here.

REGIONS = (
    ('Puget Sound', 'Puget Sound'),
    ('North Cascades', 'North Cascades'),
    ('Centeral Washington', 'Centeral Washington'),
    ('South Cascades', 'South Cascades'),
    ('Eastern Washington', 'Eastern Washington'),
)


class Hike (models.Model):
    name = models.CharField(max_length=200)
    coord = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    gain = models.CharField(max_length=200)
    highPoint = models.CharField(max_length=200)
    region = models.CharField(
        max_length=30,
        choices=REGIONS,
        default=REGIONS[0][0])
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=5000, default=None)
    directions = models.CharField(max_length=5000)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"


class Report (models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1500)
    hikeType = models.CharField(max_length=50)
    conditions = models.CharField(max_length=50)
    road = models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    bugs = models.CharField(max_length=50)
    snow = models.CharField(max_length=50)
    image = models.CharField(max_length=1000)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.user}"


class userPhoto(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User profile photo: {self.profile_id} @{self.url}"


class hikePhoto(models.Model):
    url = models.CharField(max_length=200)
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)

    def __str__(self):
        return f"Hike photo: {self.hike_id} @{self.url}"


class reportPhoto(models.Model):
    url = models.CharField(max_length=200)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"user report photo: {self.report_id} @{self.url}"
