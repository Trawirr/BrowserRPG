# Generated by Django 4.2.1 on 2023-06-11 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Memories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memory',
            options={'verbose_name_plural': 'memories'},
        ),
        migrations.RemoveField(
            model_name='memory',
            name='uses',
        ),
    ]
