from django.contrib import admin


from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class MememberInline(admin.TabularInline):
    model = Member
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "members", "create_time", "update_time"]
    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [MememberInline]




admin.site.register(Author, AuthorAdmin)

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

admin.site.register(Member)

admin.site.register(Task)

admin.site.register(Assignment)

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    filter_horizontal = ('books',)

admin.site.register(Author, AuthorAdmin)

class AuthorAdmin(admin.ModelAdmin):
    filter_vertical = ('books',)
