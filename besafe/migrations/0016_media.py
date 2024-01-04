# Generated by Django 4.2.8 on 2024-01-01 20:21

import besafe.models.contents
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('besafe', '0015_contentsportfolio_thumbnail_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('file', models.FileField(upload_to=besafe.models.contents.upload_to_media, verbose_name='파일')),
            ],
            options={
                'verbose_name': '파일',
                'verbose_name_plural': '파일목록',
                'db_table': 'media',
            },
        ),
    ]