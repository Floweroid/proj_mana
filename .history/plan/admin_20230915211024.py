from django.contrib import admin


from .models import *

admin.site.register(Question)

admin.site.register(Choice)

admin.site.register(Member)

admin.site.register(Task)

# Register your models here.
