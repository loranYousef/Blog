from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Register your models here.

class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['title','author','tags']
    list_filter = ['author','tags']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)