# Generated by Django 2.0.3 on 2018-06-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_master', '0003_auto_20180601_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialtype',
            name='description',
            field=models.TextField(default='Demo description'),
            preserve_default=False,
        ),
    ]
