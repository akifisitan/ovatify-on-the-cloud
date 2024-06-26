# Generated by Django 4.2.11 on 2024-05-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_suggestionnotification"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(
                default="pbkdf2_sha256$600000$K1JvZegDaEV2QV9Ix0KFWm$y98HSCB3SP7g0DPY3GabXW4Sf/ecPFuS5EXeQdUUE34=",
                max_length=150,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(primary_key=True, serialize=False),
        ),
    ]
