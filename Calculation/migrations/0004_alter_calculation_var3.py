# Generated by Django 5.0 on 2023-12-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculation', '0003_alter_calculation_var3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='var3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
