# Generated by Django 3.2.16 on 2024-04-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=256, verbose_name='Комментарий'),
        ),
    ]
