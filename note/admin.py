from django.contrib import admin
from .models import Note, NoteRelation

class FromNoteInline(admin.TabularInline):
    model = NoteRelation
    fk_name = 'from_note'
    extra = 2
    classes = ['collapse']


class ToNoteInline(admin.TabularInline):
    model = NoteRelation
    fk_name = 'to_note'
    extra = 2
    classes = ['collapse']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    # list_filter = (
    #     ('from_note__to_note', admin.RelatedFieldListFilter),
    #     ('to_note__from_note', admin.RelatedFieldListFilter),
    # )
    ordering = ('-created_at',)
    inlines = [ToNoteInline, FromNoteInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'content')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(NoteRelation)
class NoteRelationAdmin(admin.ModelAdmin):
    list_display = ('from_note', 'to_note')
    search_fields = ('from_note__title', 'to_note__title')
    raw_id_fields = ('from_note', 'to_note')
