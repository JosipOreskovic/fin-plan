from django.contrib import admin

from .models import Client, Task, Note

# Register your models here.

admin.site.register(Client)
admin.site.register(Task)
admin.site.register(Note)