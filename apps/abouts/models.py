from django.db import models

class About(models.Model):
    title = models.CharField(max_length=47)
    description = models.CharField(max_length=255)

    image = models.ImageField(upload_to='abouts/images/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title

