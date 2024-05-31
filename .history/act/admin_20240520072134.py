from django.contrib.admin import RelatedFieldListFilter
from django import forms
from django.contrib import admin
from .models import Note, Requirement, RequirementRelationship
from django.utils.translation import gettext_lazy as _

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


from django.utils.translation import gettext_lazy as _

from django.utils.translation import gettext_lazy as _

class RequirementFilter(admin.RelatedFieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = '%s__in' % field_path
        self.lookup_val = request.GET.getlist(self.lookup_kwarg)
        if self.lookup_val is None:  
            self.lookup_val = []  
        super().__init__(field, request, params, model, model_admin, field_path)

    def expected_parameters(self):
        return [self.lookup_kwarg]

    def choices(self, changelist):
        yield {
            'selected': not self.lookup_val,
            'query_string': changelist.get_query_string(remove=[self.lookup_kwarg]),
            'display': _('All'),
        }
        requirements = Requirement.objects.all()
        for requirement in requirements:
            selected = False
            if isinstance(self.lookup_val, list):  # Check if lookup_val is iterable
                selected = str(requirement.id) in self.lookup_val
            yield {
                'selected': selected,
                'query_string': changelist.get_query_string({self.lookup_kwarg: requirement.id}),
                'display': str(requirement),
            }


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):

    # admin view
    list_display = ( 'name', 'priority', 'start_time', 'end_time', 'created_at', 'updated_at', 'status')  
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')  
    list_filter = (
        'status',
        'priority',
        ('to_requirements__from_requirement', MultiSelectFilter),
        ('from_requirements__to_requirement', RelatedFieldListFilter),
        
    ) 
    ordering = ('-created_at',)
    inlines = [ToRequirementRelationshipInline,FromRequirementInline]
    fieldsets = (
        (None, {
            'fields': ( 'status', 'name', 'priority', 'start_time', 'end_time' )
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
