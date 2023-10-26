from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField()
    hours_worked=models.DecimalField(max_digits=5,decimal_places=2)
    description=models.TextField()

    def __str__(self):
        return f"{self.user} - {self.date}"