# Generated by Django 4.2.1 on 2023-06-13 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Regions', '0001_initial'),
        ('Enemies', '0002_alter_enemy_rank_alter_enemy_tier'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Regions.region'),
        ),
    ]