# Generated by Django 4.2.7 on 2023-11-09 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_person_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.room'),
        ),
    ]
