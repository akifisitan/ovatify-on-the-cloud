# Generated by Django 4.2.7 on 2023-11-18 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_instrument_alter_user_options_and_more'),
        ('songs', '0002_alter_album_options_alter_artist_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SongArtist',
            new_name='ArtistSong',
        ),
        migrations.RemoveField(
            model_name='song',
            name='length',
        ),
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
    ]