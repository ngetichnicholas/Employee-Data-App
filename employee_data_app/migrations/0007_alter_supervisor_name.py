# Generated by Django 3.2.5 on 2021-10-18 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data_app', '0006_alter_upload_excel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor',
            name='name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='employee_data_app.employee'),
        ),
    ]
