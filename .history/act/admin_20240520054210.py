from django import forms
from django.contrib import admin
from .models import Note, Requirement, RequirementRelationship


class RequirementRelationshipInlineForm(forms.ModelForm):
    class Meta:
        model = RequirementRelationship
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.to_requirement_id:
            requirement = self.instance.to_requirement
            for field_name in Requirement._meta.get_fields():
                if field_name.name != 'id' and hasattr(requirement, field_name.name):
                    self.fields[field_name.name].initial = getattr(requirement, field_name.name)


class FromRequirementInline(admin.StackedInline):
    model = RequirementRelationship
    # form = RequirementRelationshipForm
    fk_name = 'from_requirement'  # Specify which ForeignKey should be used
    extra = 1
    

class ToRequirementRelationshipInline(admin.StackedInline):
    model = RequirementRelationship
    form = RequirementRelationshipInlineForm
    fk_name = 'to_requirement'
    extra = 1

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        to_requirement = obj.to_requirement
        if form.cleaned_data.get('name'):
            to_requirement.name = form.cleaned_data['name']
        if form.cleaned_data.get('status'):
            to_requirement.status = form.cleaned_data['status']
        if form.cleaned_data.get('priority') is not None:
            to_requirement.priority = form.cleaned_data['priority']
        to_requirement.save()
        
        
@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'priority', 'start_time', 'end_time', 'created_at', 'updated_at')  
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')  
    list_filter = ('status', 'priority')  
    ordering = ('-created_at',)
    inlines = [FromRequirementInline,ToRequirementRelationshipInline]




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
