from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "text",
        "pub_date",
    )
    search_fields = ("text",)
    list_display_links = (
        "pk",
        "text",
    )
    list_filter = ("pub_date",)


admin.site.register(Message, MessageAdmin)
