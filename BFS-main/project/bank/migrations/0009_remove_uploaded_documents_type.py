# Generated by Django 4.2 on 2023-05-05 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_rename_loantype_uploaded_documents_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploaded_documents',
            name='type',
        ),
    ]
