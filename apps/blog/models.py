from django.conf import settings
from django.db import models

MAX_CATEGORY_NAME_LENGTH = 100
MAX_TAG_NAME_LENGTH = 50
MAX_POST_LENGTH = 200
SLUG_MAX_LENGTH = 200
STATUS_MAX_LENGTH = 10


class Category(models.Model):
    name = models.CharField(unique=True, max_length=MAX_CATEGORY_NAME_LENGTH)
    slug = models.SlugField(unique=True, max_length=SLUG_MAX_LENGTH)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=MAX_TAG_NAME_LENGTH)
    slug = models.SlugField(unique=True, max_length=SLUG_MAX_LENGTH)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=MAX_POST_LENGTH)

    slug = models.SlugField(unique=True, max_length=SLUG_MAX_LENGTH)

    body = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    tags = models.ManyToManyField(Tag, blank=True)

    status = models.TextField(
        choices=Status.choices,
        default=Status.DRAFT,
        max_length=STATUS_MAX_LENGTH,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on post: {self.post}"
