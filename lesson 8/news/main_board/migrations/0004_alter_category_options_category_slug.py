# Generated by Django 5.0.6 on 2024-05-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0003_alter_category_options_alter_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
