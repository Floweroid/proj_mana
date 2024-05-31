
from django.contrib import admin
from .models import Habit, HabitTrack, Sleep, SleepTrack, Streak
from habit import models
from django.utils import timezone
from datetime import timedelta

class HabitTrackInline(admin.TabularInline):
    model = HabitTrack
    extra = 1
    fields = ('date', 'comment', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at', 'streak_display', 'total_days_tracked')
    search_fields = ('name', 'user__username')
    list_filter = ('created_at', 'updated_at')
    inlines = [HabitTrackInline]

@admin.register(HabitTrack)
class HabitTrackAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date', 'comment', 'created_at', 'updated_at')
    search_fields = ('habit__name', 'comment')
    list_filter = ('date', 'created_at')

# Sleep


class SleepTrackInline(admin.TabularInline):
    model = SleepTrack
    extra = 1
    fields = ('date', 'start_time', 'end_time', 'get_duration', 'comment', 'created_at', 'updated_at')
    readonly_fields = ('get_duration', 'created_at', 'updated_at')
    ordering = ('-date',)

    def get_duration(self, obj):
        return obj.duration()
    get_duration.short_description = 'Duration'

@admin.register(Sleep)
class SleepAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'created_at', 'updated_at', 'streak', 'total_duration_tracked')
    search_fields = ('name', 'user__username', 'description')
    list_filter = ('user', 'created_at', 'updated_at')
    inlines = [SleepTrackInline]

    def total_duration_tracked(self, obj):
        total_duration = sum((track.duration() for track in obj.tracks.all() if track.duration()), timedelta())
        return total_duration
    total_duration_tracked.short_description = 'Total Duration Tracked'

    def streak(self, obj):
        return Streak.calculate_streak(obj.user, obj)
    streak.short_description = 'Current Streak'

@admin.register(SleepTrack)
class SleepTrackAdmin(admin.ModelAdmin):
    list_display = ('sleep', 'date', 'start_time', 'end_time', 'get_duration', 'comment', 'created_at', 'updated_at')
    search_fields = ('sleep__name', 'comment')
    list_filter = ('sleep', 'date', 'created_at', 'updated_at')
    ordering = ('-date',)
    readonly_fields = ('get_duration', 'created_at', 'updated_at')

    def get_duration(self, obj):
        return obj.duration()
    get_duration.short_description = 'Duration'