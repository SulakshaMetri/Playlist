# Generated by Django 4.2.7 on 2023-11-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicBeats', '0003_watchlater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlater',
            name='video_id',
            field=models.CharField(default='', max_length=10000000),
        ),
    ]