# Generated by Django 2.0.5 on 2018-06-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180606_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='bottlePrice',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='kegPrice',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
