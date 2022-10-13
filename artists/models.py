from django.db import models


class Artist(models.Model):
    stageName = models.CharField(max_length=100, unique=True, blank=False, null=False)
    socialLink = models.URLField(blank=True)

    def __str__(self):
        return "stageName is "+self.stageName

    class Meta:
        ordering = ('stageName',)
# Create your models here.
