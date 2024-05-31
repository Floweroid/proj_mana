from django.contrib import admin
from .models import Person, SocialRelationship

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('fName', 'lName', 'mid', 'hometown', 'created_at', 'updated_at')
    search_fields = ('fName', 'lName', 'mid', 'hometown')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(SocialRelationship)
class SocialRelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_person', 'to_person', 'relation')
    search_fields = ('from_person__fName', 'from_person__lName', 'to_person__fName', 'to_person__lName', 'relation')
    list_filter = ('relation',)
    ordering = ('from_person', 'to_person')

