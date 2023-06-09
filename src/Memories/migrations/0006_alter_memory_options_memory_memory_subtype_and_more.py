# Generated by Django 4.2.1 on 2023-06-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Memories', '0005_alter_memory_options_memory_is_equipped'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memory',
            options={'ordering': ['-is_equipped', '-rank', '-tier'], 'verbose_name_plural': 'memories'},
        ),
        migrations.AddField(
            model_name='memory',
            name='memory_subtype',
            field=models.CharField(choices=[('MELEE', 'Melee'), ('RANGED', 'Ranged'), ('ARMOR', 'Armor'), ('UTILITY', 'Utility'), ('SHIELDS', 'Shields')], default='MELEE', max_length=7),
        ),
        migrations.AlterField(
            model_name='memory',
            name='memory_type',
            field=models.CharField(choices=[('WEAPON', 'Weapon'), ('ARMOR', 'Armor'), ('UTILITY', 'Utility')], default='WEAPON', max_length=7),
        ),
    ]
