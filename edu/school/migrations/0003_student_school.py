# Generated by Django 4.1.7 on 2023-07-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.CharField(max_length=222, null=True),
        ),
    ]