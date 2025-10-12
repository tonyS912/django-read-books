from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    class Status(models.TextChoices):
        TO_READ = "TO_READ", "Will ich lesen"
        READING = "READING", "Lese ich gerade"
        FINISHED = "FINISHED", "Gelesen"
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    # note = models.TextField(max_length=600, blank=True, null=True)    Ergibt keinen Sinn, aufgrund der möglichen Masse sollten das eigenen Modelle werden.
    # tags = models.CharField(max_length=120, blank=True, null=True)    Ergibt keinen Sinn, aufgrund der möglichen Masse sollten das eigenen Modelle werden.
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TO_READ,
    )
    added_on = models.DateTimeField(default=timezone.now)
    rating = models.PositiveSmallIntegerField(validators=(MinValueValidator(0), MaxValueValidator(10)), null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=(""), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
