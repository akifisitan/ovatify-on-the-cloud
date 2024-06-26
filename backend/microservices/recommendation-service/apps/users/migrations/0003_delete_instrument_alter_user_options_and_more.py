# Generated by Django 4.2.7 on 2023-11-18 11:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_firebase_uid_alter_usersongrating_rating"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Instrument",
        ),
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="userpreferences",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="usersongrating",
            options={"ordering": ["id"]},
        ),
        migrations.RenameField(
            model_name="user",
            old_name="firebase_uid",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="userpreferences",
            old_name="preference_id",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="usersongrating",
            old_name="rating_id",
            new_name="id",
        ),
        migrations.AddField(
            model_name="friend",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="friend",
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
            model_name="friend",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="friend",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="friend",
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
            model_name="friend",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="friend",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="friend",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="friend",
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
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
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
            model_name="user",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="user",
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
            model_name="user",
            name="img_url",
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="user",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="user",
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
            model_name="userpreferences",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userpreferences",
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
            model_name="userpreferences",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="userpreferences",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="userpreferences",
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
            model_name="userpreferences",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="userpreferences",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="userpreferences",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="userpreferences",
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
            model_name="usersongrating",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created At",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="usersongrating",
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
            model_name="usersongrating",
            name="data",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="usersongrating",
            name="deleted_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Deleted At"
            ),
        ),
        migrations.AddField(
            model_name="usersongrating",
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
            model_name="usersongrating",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is Active"),
        ),
        migrations.AddField(
            model_name="usersongrating",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="Is Deleted"),
        ),
        migrations.AddField(
            model_name="usersongrating",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Updated At"
            ),
        ),
        migrations.AddField(
            model_name="usersongrating",
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
    ]
