from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('detail', kwargs={'quote_id': self.id})
        # return "/quotes/{}".format(self.id)
    def get_create_url(self):
        return reverse('create')
    
    def get_update_url(self):
        return reverse('update', kwargs={'quote_id': self.id})

    def get_delete_url(self):
        return reverse('delete', kwargs={'quote_id': self.id})