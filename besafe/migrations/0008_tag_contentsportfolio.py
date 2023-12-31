# Generated by Django 4.2.4 on 2023-12-31 22:49

import besafe.models.contents
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('besafe', '0007_contentscustomers'),
    ]


    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
            ],
        ),
        migrations.CreateModel(
            name='ContentsPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.PositiveIntegerField(default=0, verbose_name='ordering')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('banner_img', models.ImageField(upload_to=besafe.models.contents.upload_to_portfolio, verbose_name='대표이미지')),
                ('client', models.CharField(max_length=128, verbose_name='클라이언트')),
                ('biz_name', models.CharField(max_length=128, verbose_name='비즈니스명')),
                ('detail', models.CharField(max_length=128, verbose_name='사이트 바로가기')),
                ('content', models.TextField(verbose_name='내용')),
                ('tags', models.ManyToManyField(to='besafe.tag', verbose_name='태그')),
            ],
            options={
                'verbose_name': '콘텐츠 - 포트폴리오',
                'verbose_name_plural': '콘텐츠 - 포트폴리오',
                'db_table': 'contents_portfolio',
                'ordering': ['ordering'],
                'abstract': False,
            },
        ),
    ]
