from django.contrib import admin
from .models import Book


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "isbn",
        "link",
    )
    list_filter = ("author",)  # right Filter
    search_fields = ("title", "author")  # Search Field
    ordering = ("-created_at",)  # newset first
