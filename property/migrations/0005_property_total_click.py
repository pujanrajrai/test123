# Generated by Django 4.0.3 on 2022-03-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_property_location_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='total_click',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
