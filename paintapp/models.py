from django.db import models


class Files(models.Model):
    name = models.CharField(max_length=30)
    image = models.TextField()

    def __unicode__(self):
        return self.name


class Drawing(models.Model):
    image = models.TextField()  # Store the image data as text (Base64 encoded, for example)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Drawing {self.id}'
