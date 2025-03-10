from django.conf import settings
from django.contrib import admin
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    """
        We have defined the enumeration class Status by subclassing models.TextChoices
    """

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )

    title = models.CharField(max_length=250)    # CharField that translates into a varchar
    slug = models.SlugField(max_length=250)
    body = models.TextField()                   # TextField field that translates into a TEXT
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) # auto_now_add - will be saved automatically when creating an object
    updated = models.DateTimeField(auto_now=True) # will be updated automatically when saving an object
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    
    objects = models.Manager() # The default manager
    published = PublishedManager() # Our custom manager

    """
    Tip: Utilizing the auto_now_add and auto_now datetime fields in your Django models is highly
    beneficial for tracking the creation and last modification times of objects.
    """

    class Meta:
        ordering = ['-publish'] # Sorting results by the publish field.
                                # This ordering will apply by default for database queries
                                # When no specfic order is provided in the query
                                # We indicate descending order by using a hyphen before the field name, -publish.


        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
