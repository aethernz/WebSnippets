from snippets.models import Snippet,Keyword
from django.contrib import admin

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

# class PollAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),

#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question', 'pub_date', 'was_published_today')
#     list_filter = ['pub_date']
#     search_fields = ['question']
#     date_hierarchy = 'pub_date'

# admin.site.register(Poll, PollAdmin)

class SnippetAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'text', 'media', 'mediaType', 'date_added', 'last_viewed', 'width','height',],['keyword']
    list_display = ('pk','title', 'media', 'mediaType', 'url', 'width', 'height','date_added')
    save_as = True


admin.site.register([Snippet, Keyword], site=SnippetAdmin)