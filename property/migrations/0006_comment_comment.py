# Generated by Django 4.0.3 on 2022-03-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_property_total_click'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]