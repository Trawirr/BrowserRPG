# Generated by Django 4.2.1 on 2023-06-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RanksClasses', '0002_creatureclass'),
        ('Characters', '0003_remove_character_name_character_soul_core'),
    ]

    operations = [
        migrations.AddField(
            model_name='ability',
            name='agility',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ability',
            name='attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ability',
            name='defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ability',
            name='description',
            field=models.TextField(default='Description...'),
        ),
        migrations.AddField(
            model_name='ability',
            name='heal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ability',
            name='heal_percent',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ability',
            name='passage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ability',
            name='speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ability',
            name='stealth',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aspect',
            name='agility',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aspect',
            name='attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aspect',
            name='defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aspect',
            name='description',
            field=models.TextField(default='Description...'),
        ),
        migrations.AddField(
            model_name='aspect',
            name='heal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aspect',
            name='heal_percent',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='aspect',
            name='passage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aspect',
            name='prophecy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aspect',
            name='rank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RanksClasses.rank'),
        ),
        migrations.AddField(
            model_name='aspect',
            name='speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aspect',
            name='stealth',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ability',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abilities', to='Characters.character'),
        ),
        migrations.AlterField(
            model_name='aspect',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aspects', to='Characters.character'),
        ),
        migrations.CreateModel(
            name='Flaw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Description...')),
                ('attack', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('agility', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('heal', models.IntegerField(default=0)),
                ('heal_percent', models.FloatField(default=0.0)),
                ('passage', models.IntegerField(default=0)),
                ('stealth', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flaws', to='Characters.character')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]