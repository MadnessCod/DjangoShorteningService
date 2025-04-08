from django.db import models
from django.contrib.auth.models import User

from .utils import random_number_plus_characters


# Create your models here.


class BaseModel(models.Model):
    """
    BaseModel is an abstract base class that provides common methods including
        create_at and update_at
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplemented("Not Implemented method")


class Url(BaseModel):
    """
    UrlModel consists of url, auto generated short_code and access_count, and
        the use created it
    Fields:
        - user (ForeignKey): link to user who created this url
        - url (Character): original long url
        - short_code (Character): auto-generated short code
        - access_count (Integer): auto-generated, it increases each time
            someone access this url
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="user added url"
    )
    url = models.URLField(
        verbose_name="Original URL", max_length=256, null=False, blank=False
    )
    short_code = models.CharField(
        verbose_name="Short Code",
        editable=False,
        unique=True,
    )
    access_count = models.PositiveIntegerField(
        verbose_name="Access Count",
        default=0,
        blank=False,
        null=False,
    )

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = random_number_plus_characters(self.url)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"
        ordering = ["-created_at"]

    def __str__(self):
        return self.short_code
