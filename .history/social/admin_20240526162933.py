from django.contrib import admin
from .models import Person, SocialRelationship, TodoPersonRelation

class TodoPersonRelationInline(admin.TabularInline):
    model = TodoPersonRelation
    fk_name = 'person'  # The ForeignKey field to Todo in TodoPersonRelation
    extra = 1
    verbose_name = 'Todo Relation'
    verbose_name_plural = 'Todo Relations'

class SocialRelationshipInline(admin.TabularInline):
    model = SocialRelationship
    fk_name = 'from_person'
    extra = 1
    verbose_name = 'Social Relationship'
    verbose_name_plural = 'Social Relationships'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('fName', 'lName', 'mid', 'hometown', 'created_at', 'updated_at')
    search_fields = ('fName', 'lName', 'mid', 'hometown')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    inlines = [SocialRelationshipInline]

admin.site.register(Person, PersonAdmin)

class SocialRelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_person', 'to_person', 'relation')
    search_fields = ('from_person__fName', 'from_person__lName', 'to_person__fName', 'to_person__lName', 'relation')
    list_filter = ('relation',)
    ordering = ('from_person', 'to_person')

admin.site.register(SocialRelationship, SocialRelationshipAdmin)
