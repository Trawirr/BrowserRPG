# Generated by Django 4.2.1 on 2023-06-11 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RanksClasses', '0002_creatureclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(default='A memory...')),
                ('uses', models.IntegerField(default=0)),
                ('attack', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('agility', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('heal', models.IntegerField(default=0)),
                ('passage', models.IntegerField(default=0)),
                ('stealth', models.IntegerField(default=0)),
                ('rank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RanksClasses.rank')),
                ('tier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RanksClasses.tier')),
            ],
        ),
    ]
