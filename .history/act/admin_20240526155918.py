from django.contrib.admin import RelatedFieldListFilter
from django import forms
from django.contrib import admin
from .models import Note, Todo, TodoRelationship


class TodoRelationshipInlineForm(forms.ModelForm):
    status = forms.CharField(label='Status', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = TodoRelationship
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.to_Todo:
            self.fields['status'].initial = self.instance.to_Todo.status
        


class FromTodoInline(admin.StackedInline):
    model = TodoRelationship
    form = TodoRelationshipInlineForm
    fk_name = 'from_Todo'  # Specify which ForeignKey should be used
    extra = 1
    classes = ['collapse']
    

class ToTodoRelationshipInline(admin.StackedInline):
    model = TodoRelationship
    form = TodoRelationshipInlineForm
    fk_name = 'to_Todo'
    extra = 1
    classes = ['collapse']


        

class TodoRelationshipInlineForm(forms.ModelForm):
    class Meta:
        model = TodoRelationship
        fields = '__all__'


class FromTodoInline(admin.StackedInline):
    model = TodoRelationship
    fk_name = 'from_Todo'
    extra = 1
    classes = ['collapse']
    form = TodoRelationshipInlineForm  # Specify the custom form for this inline


class ToTodoRelationshipInline(admin.StackedInline):
    model = TodoRelationship
    fk_name = 'to_Todo'
    extra = 1
    classes = ['collapse']
    form = TodoRelationshipInlineForm  # Specify the custom form for this inline



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
    inlines = [ToTodoRelationshipInline,FromTodoInline]
    fieldsets = (
        (None, {
            'fields': ( 'status', 'name', 'priority', 'description','start_time', 'end_time' )
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    

    




# @admin.register(Todo)
# class TodoAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status', 'priority', 'created_at', 'updated_at', 'parent')
#     readonly_fields = ('created_at', 'updated_at')
#     search_fields = ('name', 'description')
#     list_filter = ('status', 'priority', 'created_at', 'updated_at')
#     ordering = ('-created_at',)
#     inlines = [SubTodoInline]



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

