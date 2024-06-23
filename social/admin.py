from django.contrib import admin

from note.admin import FromNoteInline, RelatedNoteInline, ToNoteInline
from social.models import Media, Person, SocialRelationship, Todo

class MediaInline(admin.TabularInline):
    model = Media
    extra = 1
    fields = ('media', 'account')
    # classes = ['collapse']

class SocialRelationshipInline(admin.TabularInline):
    model = SocialRelationship
    fk_name = 'from_person'
    extra = 1
    verbose_name = 'Social Relationship'
    verbose_name_plural = 'Social Relationships'
    classes = ['collapse']

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('fName', 'mid', 'lName', 'age', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at','age')
    search_fields = ('title', 'description')
    # list_filter = (
    #     ('from_note__to_note', admin.RelatedFieldListFilter),
    #     ('to_note__from_note', admin.RelatedFieldListFilter),
    # )
    ordering = ('-created_at',)
    inlines = [ MediaInline, SocialRelationshipInline, FromNoteInline, ToNoteInline, RelatedNoteInline ]
    fieldsets = (

        ("Person", {
            'fields': ('fName', 'mid', 'lName','age','birthdate')
        }),
        ("Note", {
            'fields': ('title', 'description', 'content'),
            'classes': ('collapse',)
        }),
        (None, {
            'fields': ('created_at', 'updated_at'),
            # 'classes': ('collapse',)
        }),
    )

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'due','duration', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at','duration')
    search_fields = ('title', 'description')
    # list_filter = (
    #     ('from_note__to_note', admin.RelatedFieldListFilter),
    #     ('to_note__from_note', admin.RelatedFieldListFilter),
    # )
    ordering = ('-created_at',)
    inlines = [ FromNoteInline, ToNoteInline, RelatedNoteInline]
    fieldsets = (


        ("Note", {
            'fields': ('title', 'description', 'content'),

        }),
        ("Time", {
            'fields': ('due', 'start_time', 'end_time', 'duration' )
        }),
        (None, {
            'fields': ('created_at', 'updated_at'),
            # 'classes': ('collapse',)
        }),
    )


