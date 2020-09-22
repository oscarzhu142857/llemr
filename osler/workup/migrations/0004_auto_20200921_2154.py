# Generated by Django 3.0.5 on 2020-09-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workup', '0003_auto_20200910_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workup',
            options={'ordering': ['-clinic_day__clinic_date'], 'permissions': [('export_pdf_Workup', 'Can export note PDF'), ('sign_Workup', 'Can sign note')]},
        ),
        migrations.AddField(
            model_name='historicalworkup',
            name='is_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workup',
            name='is_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='allergies',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='chief_complaint',
            field=models.CharField(blank=True, max_length=1000, verbose_name='CC'),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='diagnosis',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='Dx'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='fam_hx',
            field=models.TextField(blank=True, verbose_name='Family History'),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='labs_ordered_external',
            field=models.TextField(blank=True, default='', verbose_name='Labs Ordered Externally'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='labs_ordered_internal',
            field=models.TextField(blank=True, default='', verbose_name='Labs Ordered Internally'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='meds',
            field=models.TextField(blank=True, verbose_name='Medications'),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='pe',
            field=models.TextField(blank=True, verbose_name='Physical Examination'),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='ros',
            field=models.TextField(blank=True, verbose_name='ROS'),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='rx',
            field=models.TextField(blank=True, default='', verbose_name='Prescription Orders'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='soc_hx',
            field=models.TextField(blank=True, verbose_name='Social History'),
        ),
        migrations.AlterField(
            model_name='workup',
            name='allergies',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='workup',
            name='chief_complaint',
            field=models.CharField(blank=True, max_length=1000, verbose_name='CC'),
        ),
        migrations.AlterField(
            model_name='workup',
            name='diagnosis',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='Dx'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workup',
            name='fam_hx',
            field=models.TextField(blank=True, verbose_name='Family History'),
        ),
        migrations.AlterField(
            model_name='workup',
            name='labs_ordered_external',
            field=models.TextField(blank=True, default='', verbose_name='Labs Ordered Externally'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workup',
            name='labs_ordered_internal',
            field=models.TextField(blank=True, default='', verbose_name='Labs Ordered Internally'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workup',
            name='meds',
            field=models.TextField(blank=True, verbose_name='Medications'),
        ),
        migrations.AlterField(
            model_name='workup',
            name='pe',
            field=models.TextField(blank=True, verbose_name='Physical Examination'),
        ),
        migrations.AlterField(
            model_name='workup',
            name='ros',
            field=models.TextField(blank=True, verbose_name='ROS'),
        ),
        migrations.AlterField(
            model_name='workup',
            name='rx',
            field=models.TextField(blank=True, default='', verbose_name='Prescription Orders'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workup',
            name='soc_hx',
            field=models.TextField(blank=True, verbose_name='Social History'),
        ),
        migrations.RenameField(
            model_name='historicalworkup',
            old_name='A_and_P',
            new_name='a_and_p',
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='a_and_p',
            field=models.TextField(blank=True),
        ),
        migrations.RenameField(
            model_name='historicalworkup',
            old_name='HPI',
            new_name='hpi',
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='hpi',
            field=models.TextField(blank=True, verbose_name='HPI'),
        ),
        migrations.RenameField(
            model_name='historicalworkup',
            old_name='PMH_PSH',
            new_name='pmh_psh',
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='pmh_psh',
            field=models.TextField(blank=True, verbose_name='PMH/PSH'),
        ),
        migrations.RenameField(
            model_name='workup',
            old_name='A_and_P',
            new_name='a_and_p',
        ),
        migrations.AlterField(
            model_name='workup',
            name='a_and_p',
            field=models.TextField(blank=True),
        ),
        migrations.RenameField(
            model_name='workup',
            old_name='HPI',
            new_name='hpi',
        ),
        migrations.AlterField(
            model_name='workup',
            name='hpi',
            field=models.TextField(blank=True, verbose_name='HPI'),
        ),
        migrations.RenameField(
            model_name='workup',
            old_name='PMH_PSH',
            new_name='pmh_psh',
        ),
        migrations.AlterField(
            model_name='workup',
            name='pmh_psh',
            field=models.TextField(blank=True, verbose_name='PMH/PSH'),
        ),
    ]
