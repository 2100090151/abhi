# Generated by Django 4.1.7 on 2023-04-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]