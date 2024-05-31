from django import forms
from django.contrib import admin
from .models import Note, Requirement, RequirementRelationship


class RequirementRelationshipInlineForm(forms.ModelForm):
    name = forms.CharField(label='Requirement Name', max_length=100, required=False)
    status = forms.ChoiceField(label='Status', choices=Requirement.STATUS_CHOICES, required=False)
    priority = forms.IntegerField(label='Priority', required=False)

    class Meta:
        model = RequirementRelationship
        fields = ['to_requirement', 'name', 'status', 'priority']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.to_requirement_id:
            requirement = self.instance.to_requirement
            self.fields['name'].initial = requirement.name
            self.fields['status'].initial = requirement.status
            self.fields['priority'].initial = requirement.priority


class FromRequirementInline(admin.StackedInline):
    model = Requirement
    # form = RequirementRelationshipForm
    fk_name = 'from_requirement'  # Specify which ForeignKey should be used
    extra = 1
    

class ToRequirementRelationshipInline(admin.StackedInline):
    model = RequirementRelationship
    form = RequirementRelationshipInlineForm
    fk_name = 'from_requirement'
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
