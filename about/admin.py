from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.About)
admin.site.register(models.Skills)
admin.site.register(models.Educations)
admin.site.register(models.Experience)
admin.site.register(models.Service)
admin.site.register(models.Projects)
