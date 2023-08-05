# Generated by Django 3.2.8 on 2021-10-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpm', '0037_update_json_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpmrepository',
            name='last_sync_remote',
        ),
        migrations.RemoveField(
            model_name='rpmrepository',
            name='last_sync_repo_version',
        ),
        migrations.RemoveField(
            model_name='rpmrepository',
            name='last_sync_repomd_checksum',
        ),
        migrations.RemoveField(
            model_name='rpmrepository',
            name='last_sync_revision_number',
        ),
        migrations.AddField(
            model_name='rpmrepository',
            name='last_sync_details',
            field=models.JSONField(default=dict),
        ),
    ]
