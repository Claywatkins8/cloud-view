# Generated by Django 3.1.6 on 2021-02-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hike',
            name='description',
            field=models.CharField(default=None, max_length=5000),
        ),
        migrations.AddField(
            model_name='hike',
            name='directions',
            field=models.CharField(default=None, max_length=5000),
        ),
    ]
