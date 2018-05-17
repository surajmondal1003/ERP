# Generated by Django 2.0.3 on 2018-05-14 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company_branch', '0005_auto_20180509_1743'),
        ('material_master', '0002_material_is_sales'),
        ('purchaseorggroup', '0003_auto_20180509_1712'),
        ('company', '0006_auto_20180507_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_note', models.TextField()),
                ('is_approve', models.BooleanField(default=False)),
                ('is_finalised', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Company')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('purchase_grp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchaseorggroup.PurchaseGroup')),
                ('purchase_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchaseorggroup.PurchaseOrg')),
            ],
        ),
        migrations.CreateModel(
            name='RequisitionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company_branch.CompanyBranch')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='material_master.Material')),
                ('requisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase_requisition.Requisition')),
                ('storage_bin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company_branch.StorageBin')),
                ('storage_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company_branch.StorageLocation')),
                ('uom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company_branch.UOM')),
            ],
        ),
    ]
