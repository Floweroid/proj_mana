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

class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description","create_time","get_members_display"]
    fieldsets = [
        (None, {"fields": ["title", "description"]}),
        # ("Date information", {"fields": ["create_time"], "classes": ["collapse"]}),
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
