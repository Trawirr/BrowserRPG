# Generated by Django 4.2.1 on 2023-06-11 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0006_alter_character_user'),
        ('Memories', '0002_alter_memory_options_remove_memory_uses'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='character',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Characters.character'),
        ),
        migrations.AddField(
            model_name='memory',
            name='memory_type',
            field=models.CharField(choices=[('WEAPON', 'Weapon'), ('RANGED_WEAPON', 'Ranged Weapon'), ('ARMOR', 'Armor'), ('UTILITY', 'Utility')], default='WEAPON', max_length=13),
        ),
    ]