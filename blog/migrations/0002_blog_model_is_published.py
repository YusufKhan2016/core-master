# Generated by Django 4.2.2 on 2023-08-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_model',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
