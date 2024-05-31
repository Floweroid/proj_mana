from django.contrib import admin

# Register your models here.
from .models import Project, Definition, Requirement

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('project',)

class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project')
    list_filter = ('project',)

class RequirementAdmin(admin.ModelAdmin):
    list_display = ('status', 'description', 'priority', 'project')
    list_filter = ('project', 'status')

admin.site.register(Project)
admin.site.register(Definition, DefinitionAdmin)
admin.site.register(Requirement, RequirementAdmin)