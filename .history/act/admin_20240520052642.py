from django import forms
from django.contrib import admin
from .models import Note, Requirement, RequirementRelationship


class RequirementRelationshipForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = ['name', 'status', 'priority', 'start_time', 'end_time']



class FromRequirementInline(admin.StackedInline):
    model = RequirementRelationship
    # form = RequirementRelationshipForm
    fk_name = 'from_requirement'  # Specify which ForeignKey should be used
    extra = 1
    

class ToRequirementInline(admin.StackedInline):
    model = RequirementRelationship
    # form = RequirementRelationshipForm
    fk_name = 'to_requirement'  # Specify which ForeignKey should be used
    extra = 1
    

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'priority', 'start_time', 'end_time', 'created_at', 'updated_at')  
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')  
    list_filter = ('status', 'priority')  
    ordering = ('-created_at',)
    inlines = [FromRequirementInline,ToRequirementInline]




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
