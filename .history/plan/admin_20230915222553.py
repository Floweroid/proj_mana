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
    list_display = ["title", "description","create_time", "update_time","members"]
    fieldsets = [
        (None, {"fields": ["title", "description"]}),
        ("Date information", {"fields": ["create_time", "update_time"], "classes": ["collapse"]}),
    ]
    # inlines = [MememberInline]





admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

admin.site.register(Member)

admin.site.register(Task,TaskAdmin)

admin.site.register(Assignment)

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    # filter_horizontal = ('books',)
    filter_vertical = ('books',)

admin.site.register(Author, AuthorAdmin)

admin.site.register(Book)
