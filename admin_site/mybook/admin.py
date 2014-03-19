from django.contrib import admin
from .models import Poll

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Poll, AuthorAdmin)
