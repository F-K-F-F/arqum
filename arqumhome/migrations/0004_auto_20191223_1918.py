# Generated by Django 2.2.4 on 2019-12-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arqumhome', '0003_auto_20191217_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_fin_obra',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_inicio_obra',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
