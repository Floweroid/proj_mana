from django.contrib.admin import RelatedFieldListFilter
from django import forms
from django.contrib import admin

from .models import Note, Person, SocialRelationship, Todo, TodoPersonRelation, TodoRelationship


# class TodoRelationshipInlineForm(forms.ModelForm):
#     status = forms.CharField(label='Status', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

#     class Meta:
#         model = TodoRelationship
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance and self.instance.to_Todo:
#             self.fields['status'].initial = self.instance.to_Todo.status
        

# class TodoRelationshipInlineForm(forms.ModelForm):
#     class Meta:
#         model = TodoRelationship
#         fields = '__all__'


class TodoPersonRelationInline(admin.TabularInline):
    model = TodoPersonRelation
    fk_name = 'person'  # The ForeignKey field to Todo in TodoPersonRelation
    extra = 1
    verbose_name = 'Related Events'
    verbose_name_plural = 'Related Events'

class PersonTodoRelationInline(admin.TabularInline):
    model = TodoPersonRelation
    fk_name = 'todo'  # The ForeignKey field to Todo in TodoPersonRelation
    extra = 1
    verbose_name = 'Related People'
    verbose_name_plural = 'Related People'


class FromTodoInline(admin.TabularInline):
    model = TodoRelationship
    # form = TodoRelationshipInlineForm  # Specify the custom form for this inline
    fk_name = 'from_Todo'
    extra = 1
    classes = ['collapse']
    fields = ('to_status', 'to_Todo')



class ToTodoInline(admin.TabularInline):
    model = TodoRelationship
    fk_name = 'to_Todo'
    extra = 1
    classes = ['collapse']
    fields = ('from_status', 'from_Todo')
    # form = TodoRelationshipInlineForm  # Specify the custom form for this inline

class SocialRelationshipInline(admin.TabularInline):
    model = SocialRelationship
    fk_name = 'from_person'
    extra = 1
    verbose_name = 'Social Relationship'
    verbose_name_plural = 'Social Relationships'

#Admins


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    # admin view
    list_display = ( 'name', 'priority',  'start_time', 'end_time', 'created_at', 'updated_at', 'status')  
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')  
    list_filter = (
        'status',
        'priority',
        ('to_Todos__from_Todo', RelatedFieldListFilter),
        ('from_Todos__to_Todo', RelatedFieldListFilter),
        
    ) 
    ordering = ('-created_at',)
    inlines = [PersonTodoRelationInline,ToTodoInline,FromTodoInline]
    fieldsets = (
        (None, {
            'fields': ( 'status', 'name', 'priority', 'description','start_time', 'end_time' )
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('fName', 'lName', 'mid', 'hometown', 'created_at', 'updated_at')
    search_fields = ('fName', 'lName', 'mid', 'hometown')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    inlines = [TodoPersonRelationInline,SocialRelationshipInline]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(TodoRelationship)
class TodoRelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_Todo', 'to_Todo', 'created_at', 'updated_at')
    search_fields = ('from_Todo__name', 'to_Todo__name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)




@admin.register(SocialRelationship)
class SocialRelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_person', 'to_person', 'relation')
    search_fields = ('from_person__fName', 'from_person__lName', 'to_person__fName', 'to_person__lName', 'relation')
    list_filter = ('relation',)
    ordering = ('from_person', 'to_person')