# Generated by Django 5.1 on 2024-10-31 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_uz', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='features.feature')),
            ],
            options={
                'unique_together': {('feature', 'name')},
            },
        ),
    ]