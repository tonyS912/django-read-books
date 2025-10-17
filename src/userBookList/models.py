from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from book.models import Book

User = get_user_model()


class UserBook(models.Model):
    STATUS_CHOICES = [
        ("reading", "Reading"),
        ("finished", "Finished"),
        ("planned", "Planned"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planned")
    rating = models.PositiveIntegerField(null=True, blank=True)
    review = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "book")

    def __str__(self):
        return f"{self.user.username} – {self.book.title}"
