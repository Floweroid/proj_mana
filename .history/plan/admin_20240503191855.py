from django.contrib import admin


from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["title", "description","create_time","get_members_display"]
    fieldsets = [
        (None, {"fields": ["title", "description"]}),
        ("Date information", {"fields": ["create_time"], "classes": ["collapse"]}),
    ]
    # inlines = [MememberInline]




admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

# -------

class AssignmentInline(admin.TabularInline):
    model = Task.members.through
    extra = 0

class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "start_time", "status", "description", "end_time","get_members_display","create_time"]
    fieldsets = [
        (None, {"fields": ["status","title", "description"]}),
        ("Date&Time information", {"fields": ["start_time","end_time"], "classes": ["collapse"]}),
    ]
    inlines = [AssignmentInline]
    
class MemberAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline]

admin.site.register(Member)

admin.site.register(Task,TaskAdmin)

admin.site.register(Assignment)


# -------
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    # filter_horizontal = ('books',)
    filter_vertical = ('books',)

admin.site.register(Author, AuthorAdmin)

admin.site.register(Book)

# requirement

from django.contrib import admin
from .models import Project, Definition, Requirement

class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project')
    list_filter = ('project',)

class RequirementAdmin(admin.ModelAdmin):
    list_display = ('status', 'description', 'priority', 'project')
    list_filter = ('project', 'status')

admin.site.register(Project)
admin.site.register(Definition, DefinitionAdmin)
admin.site.register(Requirement, RequirementAdmin)