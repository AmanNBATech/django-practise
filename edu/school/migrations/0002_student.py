# Generated by Django 4.1.7 on 2023-07-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
    ]
