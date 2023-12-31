# Generated by Django 4.2.7 on 2023-11-28 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MusicBeats', '0002_song_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlater',
            fields=[
                ('watch_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_id', models.CharField(default='', max_length=1000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
