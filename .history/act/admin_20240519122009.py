from django.contrib import admin
from .models import Requirement, Note

class SubRequirementInline(admin.TabularInline):
    model = Requirement
    fk_name = 'parent'
    extra = 1
    fields = ('name', 'status', 'priority', 'description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    classes = ('collapse',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget.attrs['class'] = 'vTextField description'
        return formfield

    class Media:
        js = ('admin/js/inline_foldable.js',)
        css = {
            'all': ('admin/css/inline_styles.css',)
        }

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'priority', 'created_at', 'updated_at', 'parent')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('status', 'priority', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    inlines = [SubRequirementInline]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
