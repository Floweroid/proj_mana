from django.contrib import admin
from .models import Note, NotePointer

class RelatedNoteInline(admin.TabularInline):
    model = Note.related.through
    fk_name = 'from_note'
    extra = 1
    classes = ['collapse']
    verbose_name_plural = "Related Notes"

class FromNoteInline(admin.TabularInline):
    model = NotePointer
    fk_name = 'to_note'
    extra = 2
    classes = ['collapse']
    verbose_name_plural = "From Notes"

class ToNoteInline(admin.TabularInline):
    model = NotePointer
    fk_name = 'from_note'
    extra = 2
    classes = ['collapse']
    verbose_name_plural = "To Notes"



@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    # list_filter = (
    #     ('from_note__to_note', admin.RelatedFieldListFilter),
    #     ('to_note__from_note', admin.RelatedFieldListFilter),
    # )
    ordering = ('-created_at',)
    inlines = [ FromNoteInline, ToNoteInline, RelatedNoteInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'content')
        }),
        (None, {
            'fields': ('created_at', 'updated_at'),
            # 'classes': ('collapse',)
        }),
    )

@admin.register(NotePointer)
class NoteRelationAdmin(admin.ModelAdmin):
    list_display = ('id','from_note', 'to_note')
    search_fields = ('from_note__title', 'to_note__title')
    raw_id_fields = ('from_note', 'to_note')
