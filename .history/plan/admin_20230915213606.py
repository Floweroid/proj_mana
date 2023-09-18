from django.contrib import admin


from .models import *

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class TaskInline(admin.StackedInline):
    model = Task
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [TaskInline]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

admin.site.register(Member, MemberAdmin)

admin.site.register(Task)

admin.site.register(Assignment)

# Register your models here.
