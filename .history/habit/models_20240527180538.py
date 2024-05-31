from django.db import models
from django.contrib.auth.models import User  # Assuming each habit is tied to a user
from django.utils import timezone
import pytz
from datetime import timedelta

from proj_mana import settings

from datetime import timedelta, date
import pytz
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from datetime import timedelta
import pytz
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits', verbose_name='User')
    name = models.CharField(max_length=100, verbose_name='Habit Name')
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    default_timezone = models.CharField(max_length=50, default=settings.TIME_ZONE, verbose_name='Default Timezone')

    def __str__(self):
        return f"{self.name} (by {self.user.username})"

    def streak(self, user_timezone=None):
        if not user_timezone:
            user_timezone = self.default_timezone
        # Convert the current time to the user's timezone
        tz = pytz.timezone(user_timezone)
        today = timezone.now().astimezone(tz).date()
        streak_count = 0
        days = self.tracks.order_by('-date')
        for day in days:
            track_date = day.date  # track_date is a date, not datetime
            if track_date == today:
                streak_count += 1
                today -= timedelta(days=1)
            else:
                break
        return streak_count

    def streak_display(self):
        return self.streak()

    streak_display.short_description = 'Current Streak'

    def total_days_tracked(self):
        return self.tracks.count()

    total_days_tracked.short_description = 'Total Days Tracked'


    
class HabitTrack(models.Model):
    habit = models.ForeignKey(Habit, related_name='tracks', on_delete=models.CASCADE, verbose_name='Habit')
    date = models.DateField(verbose_name='Date')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return f"{self.habit.name} on {self.date}"
