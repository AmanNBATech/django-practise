# Generated by Django 4.1.7 on 2023-07-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_student_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehcile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=50)),
                ('myear', models.PositiveIntegerField()),
                ('reg_no', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('fuel', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=50)),
            ],
        ),
    ]
