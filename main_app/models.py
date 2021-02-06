from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Hike (models.Model):
    name = models.CharField(max_length=200)
    coord = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    gain = models.CharField(max_length=200)
    highPoint = models.CharField(max_length=200)
    PugetSound = 'PS'
    NorthCascades = 'NC'
    CenteralWA = 'CW'
    SouthCascades = 'SC'
    EasternWA = 'EW'
    region_choices = [
        (PugetSound, 'Puget Sound'),
        (NorthCascades, 'North Cascades'),
        (CenteralWA, 'Centeral Washington'),
        (SouthCascades, 'South Cascades'),
        (EasternWA, 'Eastern Washington'),
    ]
    hike_region = models.CharField(
        max_length=2,
        choices=region_choices,
        default=PugetSound)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=5000, default=None)
    directions = models.CharField(max_length=5000)

    def __str__(self):
        return f"{self.name}"


class Report (models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1500)
    hikeType = models.CharField(max_length=50)
    conditions = models.CharField(max_length=50)
    road = models.CharField(max_length=50)
    bugs = models.CharField(max_length=50)
    snow = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.user}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User Report photo: {self.profile_id} @{self.url}"
