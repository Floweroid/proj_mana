from django.contrib.admin import RelatedFieldListFilter
from django import forms
from django.contrib import admin
from .models import Note, Requirement, RequirementRelationship


class RequirementRelationshipInlineForm(forms.ModelForm):
    status = forms.CharField(label='Status', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = RequirementRelationship
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.to_requirement:
            self.fields['status'].initial = self.instance.to_requirement.status
        


class FromRequirementInline(admin.StackedInline):
    model = RequirementRelationship
    form = RequirementRelationshipInlineForm
    fk_name = 'from_requirement'  # Specify which ForeignKey should be used
    extra = 1
    classes = ['collapse']
    

class ToRequirementRelationshipInline(admin.StackedInline):
    model = RequirementRelationship
    form = RequirementRelationshipInlineForm
    fk_name = 'to_requirement'
    extra = 1
    classes = ['collapse']


        

class RequirementRelationshipInlineForm(forms.ModelForm):
    class Meta:
        model = RequirementRelationship
        fields = '__all__'


class FromRequirementInline(admin.StackedInline):
    model = RequirementRelationship
    fk_name = 'from_requirement'
    extra = 1
    classes = ['collapse']
    form = RequirementRelationshipInlineForm  # Specify the custom form for this inline


class ToRequirementRelationshipInline(admin.StackedInline):
    model = RequirementRelationship
    fk_name = 'to_requirement'
    extra = 1
    classes = ['collapse']
    form = RequirementRelationshipInlineForm  # Specify the custom form for this inline



@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):

    # admin view
    list_display = ( 'name', 'priority',  'start_time', 'end_time', 'created_at', 'updated_at', 'status')  
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')  
    list_filter = (
        'status',
        'priority',
        ('to_requirements__from_requirement', RelatedFieldListFilter),
        ('from_requirements__to_requirement', RelatedFieldListFilter),
        
    ) 
    ordering = ('-created_at',)
    inlines = [ToRequirementRelationshipInline,FromRequirementInline]
    fieldsets = (
        (None, {
            'fields': ( 'status', 'name', 'priority', 'description','start_time', 'end_time' )
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    

    




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

@admin.register(RequirementRelationship)
class RequirementRelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_requirement', 'to_requirement', 'created_at', 'updated_at')
    search_fields = ('from_requirement__name', 'to_requirement__name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
