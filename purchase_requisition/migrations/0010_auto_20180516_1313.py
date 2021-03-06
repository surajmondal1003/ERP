# Generated by Django 2.0.3 on 2018-05-16 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_requisition', '0009_auto_20180516_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitiondetail',
            name='material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='material_master.Material'),
        ),
        migrations.AlterField(
            model_name='requisitiondetail',
            name='uom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company_branch.UOM'),
        ),
    ]
