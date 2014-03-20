from urllib import addbase
from django.contrib import admin,messages
from .models import Poll, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ('status',)
    fields = (('title','status'),'body')
    readonly_fields = ['title']
    ordering = ['title']
    actions = ['make_published']
    # filter_horizontal = ('status',)
    actions_selection_counter = True
    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            msg = '1 row was'
        else:
            msg = '%s rows were' % rows_updated
        self.message_user(request, message='%s successfull updated' % msg,level=messages.SUCCESS)
    make_published.short_description = "Mark selected stories as published"

admin.site.register(Article, ArticleAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['question','pub_date']
    date_hierarchy = 'pub_date'
admin.site.register(Poll, AuthorAdmin)
# admin.site.disable_action('delete_selected')