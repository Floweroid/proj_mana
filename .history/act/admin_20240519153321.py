from django.contrib import admin
from .models import Requirement, Note

class SubRequirementInline(admin.StackedInline):
    model = Requirement
    fk_name = 'children'
    extra = 1
    fields = ('name', 'status', 'priority', 'start_time', 'end_time','created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    classes = ('collapse',)



# @admin.register(Requirement)
# class RequirementAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status', 'priority', 'created_at', 'updated_at', 'parent')
#     readonly_fields = ('created_at', 'updated_at')
#     search_fields = ('name', 'description')
#     list_filter = ('status', 'priority', 'created_at', 'updated_at')
#     ordering = ('-created_at',)
#     inlines = [SubRequirementInline]

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'priority', 'start_time', 'end_time','created_at', 'updated_at')  # Display these fields in the list view
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')  # Add these fields to the search bar
    list_filter = ('status', 'priority')  # Add filters for these fields
    ordering = ('-created_at',)
    inlines = [SubRequirementInline]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
