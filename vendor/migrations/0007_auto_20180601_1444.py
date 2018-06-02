# Generated by Django 2.0.3 on 2018-06-01 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_vendortype_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vendoraccount',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vendoraddress',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]