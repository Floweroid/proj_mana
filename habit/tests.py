from django.test import TestCase
from django.contrib.auth.models import User
from .models import Habit, HabitTrack
from django.utils import timezone
import pytz

class HabitModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test habit
        self.habit = Habit.objects.create(user=self.user, name='Test Habit', default_timezone='UTC')

    def create_habit_tracks(self, dates):
        # Create habit tracks for the given dates
        for date in dates:
            HabitTrack.objects.create(habit=self.habit, date=date)

    def test_streak_no_tracks(self):
        # Test with no habit tracks
        self.assertEqual(self.habit.streak(), 0)

    def test_streak_single_day(self):
        # Test with a single habit track for today
        self.create_habit_tracks([timezone.now().date()])
        self.assertEqual(self.habit.streak(), 1)

    def test_streak_multiple_days(self):
        # Test with multiple consecutive habit tracks
        today = timezone.now().date()
        self.create_habit_tracks([today, today - timezone.timedelta(days=1), today - timezone.timedelta(days=2)])
        self.assertEqual(self.habit.streak(), 3)

    def test_streak_with_gap(self):
        # Test with a gap in habit tracks
        today = timezone.now().date()
        self.create_habit_tracks([today, today - timezone.timedelta(days=2)])
        self.assertEqual(self.habit.streak(), 1)

    def test_streak_with_timezone(self):
        # Test with a different timezone
        self.habit.default_timezone = 'Asia/Kolkata'
        self.habit.save()
        
        tz = pytz.timezone('Asia/Kolkata')
        today = timezone.now().astimezone(tz).date()
        
        self.create_habit_tracks([today, today - timezone.timedelta(days=1), today - timezone.timedelta(days=2)])
        self.assertEqual(self.habit.streak(user_timezone='Asia/Kolkata'), 3)

    def test_streak_with_default_timezone(self):
        # Test with default timezone setting
        tz = pytz.timezone('UTC')
        today = timezone.now().astimezone(tz).date()
        
        self.create_habit_tracks([today, today - timezone.timedelta(days=1), today - timezone.timedelta(days=2)])
        self.assertEqual(self.habit.streak(), 3)

# Run the tests
if __name__ == "__main__":
    import unittest
    unittest.main()
