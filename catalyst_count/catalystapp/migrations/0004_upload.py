# Generated by Django 4.2.3 on 2024-02-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalystapp', '0003_alter_employee_keyword'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
