# Generated by Django 2.0.3 on 2018-05-31 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0002_remove_contractor_contact_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='gst_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]