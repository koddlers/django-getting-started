from django.db import models
from datetime import time


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    def __str__(self):
        return f"Meeting: {self.title}, for {self.duration} hr(s), on {self.date} starts at: {self.start_time}"
