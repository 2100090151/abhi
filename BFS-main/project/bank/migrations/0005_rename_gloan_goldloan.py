# Generated by Django 4.1.7 on 2023-04-02 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_rename_firstname_gloan_fname_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='gloan',
            new_name='GoldLoan',
        ),
    ]