# Generated by Django 2.0.5 on 2020-03-28 16:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modulka', '0002_auto_20200328_1542'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
