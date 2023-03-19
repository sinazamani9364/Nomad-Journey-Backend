from django.db import models
from accounts.models import *


class Announcement(models.Model):
    announcer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    id = models.AutoField(primary_key=True)

    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    arrival_date_is_flexible = models.BooleanField(null=True)
    departure_date_is_flexible = models.BooleanField(null=True)
    message = models.TextField(max_length=500, null=True)
    timestamp_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'This is an announcement with ID ' + str(self.id) + " and the announcer is "+str(self.announcer)+ '.' 
