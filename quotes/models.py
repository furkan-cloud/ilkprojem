from django.db import models

# Create your models here.

class Quote(models.Model):
    name = models.CharField(max_length=100, verbose_name='Söz Konusu')
    description = models.TextField(verbose_name='Söz')
    image = models.CharField(max_length=50, verbose_name='Resim')
    created_date = models.DateTimeField(auto_now_add=True)
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/'+ self.image