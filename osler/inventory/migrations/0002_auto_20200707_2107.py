# Generated by Django 3.0.5 on 2020-07-08 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='lot_number',
            field=models.CharField(max_length=100),
        ),
    ]
