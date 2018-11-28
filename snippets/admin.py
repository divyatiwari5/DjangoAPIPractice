from django.contrib import admin
from .models import Snippet
# Register your models here.

class SnippetClass(admin.ModelAdmin):
    list_display = ('title', 'code', 'boolean', 'language', 'style')

admin.site.register(Snippet, SnippetClass)