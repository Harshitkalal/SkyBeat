# Generated by Django 2.0.2 on 2019-08-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20190802_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file_type',
            field=models.FileField(upload_to=''),
        ),
    ]
