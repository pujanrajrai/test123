# Generated by Django 4.0.3 on 2022-03-08 05:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_comment_comment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='propertybookmark',
            unique_together={('user', 'property')},
        ),
    ]
