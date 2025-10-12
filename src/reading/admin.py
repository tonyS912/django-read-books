from django.contrib import admin
from django.utils.html import format_html

from .models import Book

# Register your models here.


@admin.display(description="Status")
def colored_status(obj):
    color = {
        "TO_READ": "gray",
        "READING": "orange",
        "FINISHED": "green",
    }
    color = color.get(obj.status, "black")
    return format_html('<b style="color: {}">{}</b>', color, obj.get_status_display())


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "isbn",
        colored_status,
        "rating",
    )
    list_filter = ("status", "author")  # rechte Filterleiste
    search_fields = ("title", "author")  # Suchfeld oben
    ordering = ("-added_on",)  # neueste zuerst
