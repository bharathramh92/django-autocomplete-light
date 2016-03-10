from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)

    test = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='related_publisher_test_models'
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    test = models.ManyToManyField(
        'self',
        blank=True,
        null=True,
        related_name='related__author_test_models'
    )

    def __str__(self):
        return self.name

