# Generated by Django 2.0.1 on 2024-06-21 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooftop', '0004_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='review',
            new_name='comment',
        ),
    ]