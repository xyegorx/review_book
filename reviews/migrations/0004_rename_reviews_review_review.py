# Generated by Django 4.2.5 on 2023-11-08 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviews',
            new_name='review',
        ),
    ]
