# Generated by Django 5.0.4 on 2024-05-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Порода')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cats_photoes', verbose_name='Фото')),
                ('slug', models.SlugField(verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Котик',
                'verbose_name_plural': 'Котики',
                'ordering': ['name'],
            },
        ),
    ]
