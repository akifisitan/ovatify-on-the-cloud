# Generated by Django 4.2.7 on 2023-11-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("songs", "0004_alter_song_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="img_url",
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="artist",
            name="img_url",
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="genre",
            name="img_url",
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="song",
            name="img_url",
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
