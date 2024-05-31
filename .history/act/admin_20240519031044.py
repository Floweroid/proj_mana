# admin.py
from django.contrib import admin
from .models import Requirement, Note

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('status', 'priority', 'created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
