# Generated by Django 2.0.5 on 2020-03-28 15:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modulka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]