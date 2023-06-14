# Generated by Django 4.2.1 on 2023-06-11 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Characters', '0005_remove_ability_heal_percent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to=settings.AUTH_USER_MODEL),
        ),
    ]
