# Generated by Django 2.0.5 on 2020-03-28 16:25

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modulka', '0003_auto_20200328_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]