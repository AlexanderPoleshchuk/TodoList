from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_completed')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_completed',)
    list_filter = ('is_completed',)



admin.site.register(Task, TaskAdmin)
