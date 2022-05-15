# Generated by Django 4.0.3 on 2022-03-07 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_state_alter_property_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location_state',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='property.state'),
            preserve_default=False,
        ),
    ]
