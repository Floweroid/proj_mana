from django.contrib import admin
from .models import Habit, HabitTrack

class HabitTrackInline(admin.TabularInline):
    model = HabitTrack
    extra = 1

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at', 'streak_display', 'total_days_tracked')
    search_fields = ('name', 'user__username')
    list_filter = ('created_at', 'updated_at')
    inlines = [HabitTrackInline]

@admin.register(HabitTrack)
class HabitTrackAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date', 'created_at', 'updated_at')
    search_fields = ('habit__name',)
    list_filter = ('date', 'created_at')

