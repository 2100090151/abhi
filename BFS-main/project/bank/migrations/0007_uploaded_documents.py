# Generated by Django 4.2 on 2023-05-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_eduloan_homeloan_personalloan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploaded_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('loantype', models.CharField(max_length=30)),
                ('aadhar', models.FileField(upload_to='')),
                ('pan', models.FileField(upload_to='')),
            ],
        ),
    ]