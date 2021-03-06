# Generated by Django 2.0.3 on 2018-05-14 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GSTrates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst_pattern', models.CharField(max_length=100)),
                ('igst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cgst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sgst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
