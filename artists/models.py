from django.conf import settings
from django.db import models


class Artist(models.Model):
    stageName = models.CharField(max_length=100, unique=True, blank=False, null=False)
    socialLink = models.URLField(blank=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='artists', on_delete=models.CASCADE)

    def __str__(self):
        return "stageName is " + self.stageName

    class Meta:
        ordering = ('stageName',)
