# Generated by Django 3.2.17 on 2023-02-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20230228_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='manual_views',
            field=models.CharField(blank=True, default='', max_length=1000),
            preserve_default=False,
        ),
    ]
