# Generated by Django 3.2.5 on 2021-10-17 19:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data_app', '0005_alter_upload_excel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='excel_file',
            field=models.FileField(upload_to='excel/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xlsx'])]),
        ),
    ]