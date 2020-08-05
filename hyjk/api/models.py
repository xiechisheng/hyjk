from django.db import models

# Create your models here.
class user_info(models.Model):
    login = models.CharField(max_length=64, unique=True, null=False)
    password = models.CharField(max_length=64, null=False)
    nickname = models.CharField(max_length=64, null=False)
    enable = models.PositiveSmallIntegerField(null=False, default=1)


class rtsp_info(models.Model):
    ip=models.CharField(max_length=64,unique=True,null=False)
    port=models.IntegerField(null=True, default=1026)
    name=models.CharField(max_length=64,null=False)
    longitude = models.CharField(max_length=64, null=False)
    latitude = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=256, null=False, default=0)
    observation_area=models.CharField(max_length=256, null=False, default=0)
    observation_target= models.CharField(max_length=256, null=False, default=0)
    enable = models.PositiveSmallIntegerField(null=False, default=1)
    bin_id=models.IntegerField(null=False, default=1026)
    tide_level_name=models.CharField(max_length=64, null=True)
    tide_level_code=models.CharField(max_length=64, null=True)
    wave_heigh_name=models.CharField(max_length=64, null=True)
    wave_heigh_code=models.CharField(max_length=64, null=True)
    wave_direction_name=models.CharField(max_length=64, null=True)
    wave_direction_code=models.CharField(max_length=64, null=True)


