from django.contrib import admin
from .models import Task

# Register your models here.
class taskAdmin(admin.ModelAdmin):
    list_display = ("task", "isCompleted", "updatedAt")
    list_filter = ("isCompleted",)


admin.site.register(Task, taskAdmin)