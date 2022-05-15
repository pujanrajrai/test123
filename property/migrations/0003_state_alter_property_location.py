# Generated by Django 4.0.3 on 2022-03-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
