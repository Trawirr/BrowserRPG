# Generated by Django 4.2.1 on 2023-06-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0002_character_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='name',
        ),
        migrations.AddField(
            model_name='character',
            name='soul_core',
            field=models.IntegerField(default=0),
        ),
    ]
