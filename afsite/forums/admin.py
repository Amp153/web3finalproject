from django.contrib import admin
from .models import Post, Title

class PostInLine(admin.TabularInline):
    model = Post
    extra = 1

class TitleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [PostInLine]
    list_display = ('title_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title_text']

admin.site.register(Title, TitleAdmin)