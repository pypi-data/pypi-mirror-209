# Generated by Django 3.2.5 on 2021-07-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpm', '0037_DATA_remove_rpmrepository_sub_repo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulemd',
            name='artifacts',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='modulemd',
            name='dependencies',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='modulemddefaults',
            name='profiles',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='changelogs',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='conflicts',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='enhances',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='files',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='obsoletes',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='provides',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='recommends',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='requires',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='suggests',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='package',
            name='supplements',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='packagecategory',
            name='desc_by_lang',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='packagecategory',
            name='group_ids',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='packagecategory',
            name='name_by_lang',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='packageenvironment',
            name='desc_by_lang',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='packageenvironment',
            name='group_ids',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='packageenvironment',
            name='name_by_lang',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='packageenvironment',
            name='option_ids',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='packagegroup',
            name='desc_by_lang',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='packagegroup',
            name='name_by_lang',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='packagegroup',
            name='packages',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='packagelangpacks',
            name='matches',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='rpmrepository',
            name='original_checksum_types',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='updatecollection',
            name='module',
            field=models.JSONField(null=True),
        ),
    ]
