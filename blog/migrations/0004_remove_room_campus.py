# Generated by Django 4.2.7 on 2023-11-09 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_person_available_remove_person_published_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='campus',
        ),
    ]
