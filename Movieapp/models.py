from django.db import models
# Create your models here.

class Actor(models.Model):
    Aname = models.CharField(max_length=100)
    Aage = models.IntegerField()
    Agendor = models.CharField(max_length=50)
    class Meta:
        db_table='Actor_Info'

class Movie(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    Movi_Act = models.ManyToManyField(Actor)
    class Meta:
        db_table='Movie_Info'

# class Movie_Actor(models.Model):
#     movie = models.ForeignKey (Movie,on_delete=models.CASCADE)
#     actor = models.ForeignKey(Actor,on_delete=models.CASCADE)
#     date_released = models.DateField()
#     # invite_reason = models.CharField(max_length=64)
#
#     class Meta:
#         db_table='Movie_Actor_Info'