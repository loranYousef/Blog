from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Kontakt,Post , Category 

# Register your models here.

class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Kontakt)
# admin.site.register(Post,PostAdmin)
# admin.site.register(Category)
