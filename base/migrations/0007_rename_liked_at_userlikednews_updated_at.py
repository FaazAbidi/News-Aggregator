# Generated by Django 4.1.7 on 2023-02-19 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_newsarticle_published_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlikednews',
            old_name='liked_at',
            new_name='updated_at',
        ),
    ]