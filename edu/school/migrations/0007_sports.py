# Generated by Django 4.1.7 on 2023-07-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_vehcile'),
    ]

    operations = [
        migrations.CreateModel(
            name='sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basketball', models.PositiveIntegerField()),
                ('football', models.PositiveIntegerField()),
                ('kabbadi', models.PositiveIntegerField()),
                ('cricket', models.PositiveIntegerField()),
                ('volleyball', models.PositiveIntegerField()),
            ],
        ),
    ]