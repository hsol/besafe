# Generated by Django 4.2.4 on 2024-01-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('besafe', '0013_contentsconsulting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentsnews',
            name='subtitle',
            field=models.CharField(max_length=512, verbose_name='부제목'),
        ),
    ]