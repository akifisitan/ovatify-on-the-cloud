# Generated by Django 4.2.7 on 2023-12-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_friendgroup_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendgroup',
            name='name',
            field=models.CharField(default='New Friend Group', max_length=200),
        ),
    ]
