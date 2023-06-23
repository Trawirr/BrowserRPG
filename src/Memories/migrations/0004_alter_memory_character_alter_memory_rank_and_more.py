# Generated by Django 4.2.1 on 2023-06-14 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RanksClasses', '0002_creatureclass'),
        ('Characters', '0006_alter_character_user'),
        ('Memories', '0003_memory_character_memory_memory_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='character',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memories', to='Characters.character'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='rank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='memories', to='RanksClasses.rank'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='memories', to='RanksClasses.tier'),
        ),
    ]