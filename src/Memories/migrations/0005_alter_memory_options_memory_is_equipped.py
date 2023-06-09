# Generated by Django 4.2.1 on 2023-06-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Memories', '0004_alter_memory_character_alter_memory_rank_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memory',
            options={'ordering': ['rank', 'tier'], 'verbose_name_plural': 'memories'},
        ),
        migrations.AddField(
            model_name='memory',
            name='is_equipped',
            field=models.BooleanField(default=False),
        ),
    ]
