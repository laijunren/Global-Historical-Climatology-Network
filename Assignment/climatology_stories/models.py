from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Year(models.Model):
    ID = models.IntegerField(primary_key=True)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.ID}, {self.year}"

class Climate(models.Model):
    year_ID = models.ForeignKey('Year', on_delete=models.CASCADE, related_name='climates')
    year = models.IntegerField()
    month = models.IntegerField()
    lat = models.TextField()
    lon_175_180W = models.IntegerField()
    lon_170_175W = models.IntegerField()
    lon_165_170W = models.IntegerField()
    lon_160_165W = models.IntegerField()
    lon_155_160W = models.IntegerField()
    lon_150_155W = models.IntegerField()
    lon_145_150W = models.IntegerField()
    lon_140_145W = models.IntegerField()
    lon_135_140W = models.IntegerField()
    lon_130_135W = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year_ID}, {self.year}, {self.month}, {self.lat}, {self.lon_175_180W}, {self.lon_170_175W}, {self.lon_165_170W}, {self.lon_160_165W}, {self.lon_155_160W}, {self.lon_150_155W}, {self.lon_145_150W}, {self.lon_140_145W}, {self.lon_135_140W}, {self.lon_130_135W}, {self.created_date}"