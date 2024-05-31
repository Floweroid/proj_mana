from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from pytz import timezone  # Assuming each habit is tied to a user

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits', verbose_name='User')
    name = models.CharField(max_length=100, verbose_name='Habit Name')
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return f"{self.name} (by {self.user.username})"

    def streak(self):
        today = timezone.now().date()
        streak_count = 0
        days = self.tracks.order_by('-date')
        for day in days:
            if day.date == today:
                streak_count += 1
                today -= timedelta(days=1)
            else:
                break
        return streak_count

class HabitTrack(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='tracks', verbose_name='Habit')
    date = models.DateField(verbose_name='Date')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        unique_together = ('habit', 'date')  # Ensure a habit can be tracked only once per day

    def __str__(self):
        return f"{self.habit.name} tracked on {self.date}"
