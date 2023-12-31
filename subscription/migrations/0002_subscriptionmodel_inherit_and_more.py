# Generated by Django 4.2.4 on 2023-08-20 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionmodel',
            name='inherit',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='subscription.subscriptionmodel'),
        ),
        migrations.AlterField(
            model_name='subscriptionmodelservice',
            name='service_type',
            field=models.CharField(choices=[('MAIN', '주요 서비스'), ('ETC', '기타 부대 업무')], max_length=8, verbose_name='서비스종류'),
        ),
    ]
