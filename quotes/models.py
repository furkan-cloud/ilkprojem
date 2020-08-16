from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Quote(models.Model):
    user = models.ForeignKey('auth.User',verbose_name='Yazar',on_delete=models.CASCADE, related_name='quotes')
    name = models.CharField(max_length=100, verbose_name='Söz Konusu')
    description = RichTextField(verbose_name='Söz')
    image = models.ImageField(null=True, blank=True, verbose_name='Resim')
    created_date = models.DateTimeField(auto_now_add=True)
    isPublished = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, editable=False, max_length=110)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/'+ self.image

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
        # return "/quotes/{}".format(self.id)
    def get_create_url(self):
        return reverse('create')
    
    def get_update_url(self):
        return reverse('update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('delete', kwargs={'slug': self.slug})
   
    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Quote.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Quote, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):

    quote = models.ForeignKey('quotes.Quote', related_name='comments', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, verbose_name='isim')
    content = models.TextField(verbose_name='Yorum')

    created_date = models.DateTimeField(auto_now_add=True)