from django import forms
from django.contrib import admin
from .models import Note, Requirement, RequirementRelationship


class RequirementRelationshipForm(forms.ModelForm):
    class Meta:
        model = RequirementRelationship
        fields = ['to_requirement']



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
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "to_requirement":
            kwargs["queryset"] = Requirement.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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
