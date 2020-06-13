from django.contrib import admin

from .models import News

# Register your models here.

admin.site.register(News)


class NewsAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    class Meta:
        model = News