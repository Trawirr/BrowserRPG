# Generated by Django 4.2.1 on 2023-06-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New region...', max_length=50)),
                ('gate', models.BooleanField(default=False)),
                ('adjacent_regions', models.ManyToManyField(blank=True, null=True, to='Regions.region')),
            ],
        ),
    ]