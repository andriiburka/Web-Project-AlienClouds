from django.contrib import admin

# Register your models here.
from projects_app.models.project import Project
admin.site.register(Project)
