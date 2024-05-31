from django import forms
from django.contrib import admin
from .models import Note, Requirement, RequirementRelationship


class RequirementRelationshipInlineForm(forms.ModelForm):

    class Meta:
        model = RequirementRelationship
        fields = '__all__'
        


class FromRequirementInline(admin.StackedInline):
    model = RequirementRelationship

    fk_name = 'from_requirement'  # Specify which ForeignKey should be used
    extra = 1
    classes = ['collapse']
    

class ToRequirementRelationshipInline(admin.StackedInline):
    model = RequirementRelationship

    fk_name = 'to_requirement'
    extra = 1
    classes = ['collapse']


        
        
@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('status', 'name', 'priority', 'start_time', 'end_time', 'created_at', 'updated_at')  
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')  
    list_filter = ('status', 'priority')  
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {
            'fields': ('status', 'name', 'priority', 'start_time', 'end_time')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
        ('Related Requirements', {
            'fields': ('from_requirements', 'to_requirements'),  # Include inline models here
            'classes': ('collapse',),
            'description': 'Inline models will be displayed here',
        }),
    )

    inlines = [FromRequirementInline, ToRequirementRelationshipInline]
    




# @admin.register(Requirement)
# class RequirementAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status', 'priority', 'created_at', 'updated_at', 'parent')
#     readonly_fields = ('created_at', 'updated_at')
#     search_fields = ('name', 'description')
#     list_filter = ('status', 'priority', 'created_at', 'updated_at')
#     ordering = ('-created_at',)
#     inlines = [SubRequirementInline]



@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
