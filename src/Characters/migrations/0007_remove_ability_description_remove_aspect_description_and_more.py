# Generated by Django 4.2.1 on 2023-06-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0006_alter_character_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ability',
            name='description',
        ),
        migrations.RemoveField(
            model_name='aspect',
            name='description',
        ),
        migrations.RemoveField(
            model_name='flaw',
            name='description',
        ),
        migrations.AddField(
            model_name='ability',
            name='name',
            field=models.TextField(default='Name...'),
        ),
        migrations.AddField(
            model_name='aspect',
            name='name',
            field=models.TextField(default='Name...'),
        ),
        migrations.AddField(
            model_name='flaw',
            name='name',
            field=models.TextField(default='Name...'),
        ),
    ]
