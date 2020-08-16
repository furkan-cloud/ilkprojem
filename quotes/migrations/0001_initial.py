# Generated by Django 3.0.9 on 2020-08-16 11:33

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Söz Konusu')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Söz')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Resim')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('isPublished', models.BooleanField(default=True)),
                ('slug', models.SlugField(editable=False, max_length=110, unique=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
