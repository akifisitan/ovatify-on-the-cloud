# Generated by Django 4.2.7 on 2023-11-18 11:55

from datetime import timedelta
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_delete_instrument_alter_user_options_and_more"),
        ("songs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="album",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="artist",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="instrument",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="song",
            options={"ordering": ["id"]},
        ),
        migrations.RenameField(
            model_name="album",
            old_name="album_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="artist",
            old_name="artist_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="genre",
            old_name="genre_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="genre",
            old_name="genre_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="instrument",
            old_name="instrument_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="instrument",
            old_name="instrument_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="instrument",
            old_name="instrument_type",
            new_name="type",
        ),
        migrations.RenameField(
            model_name="song",
            old_name="song_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="song",
            old_name="track_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="song",
            old_name="recommended_environment",
            new_name="recorded_environment",
        ),
        migrations.AddField(
            model_name="album",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="album",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_created_by",
                to="users.user",
                verbose_name="Created By",
            ),
        ),
        migrations.AddField(
            model_name="album",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="album",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="album",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_deleted_by",
                to="users.user",
                verbose_name="Deleted By",
            ),
        ),
        migrations.AddField(
            model_name="album",
            name="img_url",
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="album",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="album",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="album",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="album",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_updated_by",
                to="users.user",
                verbose_name="Updated By",
            ),
        ),
        migrations.AddField(
            model_name="albumsong",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="albumsong",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_created_by",
                to="users.user",
                verbose_name="Created By",
            ),
        ),
        migrations.AddField(
            model_name="albumsong",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="albumsong",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="albumsong",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_deleted_by",
                to="users.user",
                verbose_name="Deleted By",
            ),
        ),
        migrations.AddField(
            model_name="albumsong",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="albumsong",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="albumsong",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="albumsong",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_updated_by",
                to="users.user",
                verbose_name="Updated By",
            ),
        ),
        migrations.AddField(
            model_name="artist",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="artist",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_created_by",
                to="users.user",
                verbose_name="Created By",
            ),
        ),
        migrations.AddField(
            model_name="artist",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="artist",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="artist",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_deleted_by",
                to="users.user",
                verbose_name="Deleted By",
            ),
        ),
        migrations.AddField(
            model_name="artist",
            name="img_url",
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="artist",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="artist",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="artist",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="artist",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_updated_by",
                to="users.user",
                verbose_name="Updated By",
            ),
        ),
        migrations.AddField(
            model_name="genre",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="genre",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_created_by",
                to="users.user",
                verbose_name="Created By",
            ),
        ),
        migrations.AddField(
            model_name="genre",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="genre",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="genre",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_deleted_by",
                to="users.user",
                verbose_name="Deleted By",
            ),
        ),
        migrations.AddField(
            model_name="genre",
            name="img_url",
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="genre",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="genre",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="genre",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="genre",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_updated_by",
                to="users.user",
                verbose_name="Updated By",
            ),
        ),
        migrations.AddField(
            model_name="genresong",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="genresong",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_created_by",
                to="users.user",
                verbose_name="Created By",
            ),
        ),
        migrations.AddField(
            model_name="genresong",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="genresong",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="genresong",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_deleted_by",
                to="users.user",
                verbose_name="Deleted By",
            ),
        ),
        migrations.AddField(
            model_name="genresong",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="genresong",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="genresong",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="genresong",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_updated_by",
                to="users.user",
                verbose_name="Updated By",
            ),
        ),
        migrations.AddField(
            model_name="instrument",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="instrument",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_created_by",
                to="users.user",
                verbose_name="Created By",
            ),
        ),
        migrations.AddField(
            model_name="instrument",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="instrument",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="instrument",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_deleted_by",
                to="users.user",
                verbose_name="Deleted By",
            ),
        ),
        migrations.AddField(
            model_name="instrument",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="instrument",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="instrument",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="instrument",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_updated_by",
                to="users.user",
                verbose_name="Updated By",
            ),
        ),
        migrations.AddField(
            model_name="instrumentsong",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="instrumentsong",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_created_by",
                to="users.user",
                verbose_name="Created By",
            ),
        ),
        migrations.AddField(
            model_name="instrumentsong",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="instrumentsong",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="instrumentsong",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_deleted_by",
                to="users.user",
                verbose_name="Deleted By",
            ),
        ),
        migrations.AddField(
            model_name="instrumentsong",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="instrumentsong",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="instrumentsong",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="instrumentsong",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_updated_by",
                to="users.user",
                verbose_name="Updated By",
            ),
        ),
        migrations.AddField(
            model_name="song",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="song",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_created_by",
                to="users.user",
                verbose_name="Created By",
            ),
        ),
        migrations.AddField(
            model_name="song",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="song",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="song",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_deleted_by",
                to="users.user",
                verbose_name="Deleted By",
            ),
        ),
        migrations.AddField(
            model_name="song",
            name="img_url",
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="song",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="song",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="song",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="song",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_updated_by",
                to="users.user",
                verbose_name="Updated By",
            ),
        ),
        migrations.AddField(
            model_name="songartist",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="songartist",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_created_by",
                to="users.user",
                verbose_name="Created By",
            ),
        ),
        migrations.AddField(
            model_name="songartist",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="songartist",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="songartist",
            name="deleted_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_deleted_by",
                to="users.user",
                verbose_name="Deleted By",
            ),
        ),
        migrations.AddField(
            model_name="songartist",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="songartist",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="songartist",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="songartist",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_updated_by",
                to="users.user",
                verbose_name="Updated By",
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="version",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
