from django.contrib import admin
from .models import poll

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(poll, AuthorAdmin)
