from django import forms
from django.contrib import admin
from .models import Note, Requirement, RequirementRelationship


from django import forms
from .models import Requirement, RequirementRelationship

class RequirementRelationshipInlineForm(forms.ModelForm):
    class Meta:
        model = RequirementRelationship
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.to_requirement_id:
            requirement = self.instance.to_requirement
            for field in Requirement._meta.fields:
                field_name = field.name
                if field_name != 'id':
                    field_value = getattr(requirement, field_name)
                    if isinstance(field, models.DateField):
                        self.fields[field_name] = forms.DateField(label=field.verbose_name, initial=field_value, required=False)
                    elif isinstance(field, models.DateTimeField):
                        self.fields[field_name] = forms.DateTimeField(label=field.verbose_name, initial=field_value, required=False)
                    elif isinstance(field, models.TimeField):
                        self.fields[field_name] = forms.TimeField(label=field.verbose_name, initial=field_value, required=False)
                    elif isinstance(field, models.CharField):
                        self.fields[field_name] = forms.CharField(label=field.verbose_name, max_length=field.max_length, initial=field_value, required=False)
                    elif isinstance(field, models.TextField):
                        self.fields[field_name] = forms.CharField(label=field.verbose_name, widget=forms.Textarea, initial=field_value, required=False)
                    elif isinstance(field, models.IntegerField):
                        self.fields[field_name] = forms.IntegerField(label=field.verbose_name, initial=field_value, required=False)
                    elif isinstance(field, models.DecimalField):
                        self.fields[field_name] = forms.DecimalField(label=field.verbose_name, initial=field_value, required=False)
                    elif isinstance(field, models.BooleanField):
                        self.fields[field_name] = forms.BooleanField(label=field.verbose_name, initial=field_value, required=False)
                    elif isinstance(field, models.FloatField):
                        self.fields[field_name] = forms.FloatField(label=field.verbose_name, initial=field_value, required=False)
                    # Add more field types as needed



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
        for field_name in form.cleaned_data:
            if hasattr(to_requirement, field_name):
                setattr(to_requirement, field_name, form.cleaned_data[field_name])
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
