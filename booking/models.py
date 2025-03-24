from django.db import models
from django.contrib.auth.models import User

class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending'
    )

    class Meta:
        unique_together = ('facility', 'date')  # Ensure only one booking per facility per date

    def __str__(self):
        return f"{self.user.username} booked {self.facility.name} on {self.date}"
