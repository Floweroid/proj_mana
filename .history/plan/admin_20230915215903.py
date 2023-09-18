from django.contrib import admin


from .models import *

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class MememberInline(admin.StackedInline):
    model = Member
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [MememberInline]



admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

admin.site.register(Member)

admin.site.register(Task)

admin.site.register(Assignment)

# Register your models here.
