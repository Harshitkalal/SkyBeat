# Generated by Django 2.0.2 on 2019-08-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190704_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file_type',
            field=models.FileField(max_length=10, upload_to=''),
        ),
    ]