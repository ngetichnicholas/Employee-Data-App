# Generated by Django 3.2.5 on 2021-10-17 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supervisor',
            old_name='supervisor',
            new_name='name',
        ),
    ]
