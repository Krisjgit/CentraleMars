# Generated by Django 4.2.7 on 2023-11-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_room_campus_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='available',
        ),
        migrations.RemoveField(
            model_name='person',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='person',
            name='planet',
            field=models.CharField(default='Earth', max_length=128),
        ),
    ]
