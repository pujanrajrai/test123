# Generated by Django 4.0.3 on 2022-03-08 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_comments_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='property',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='property.property'),
            preserve_default=False,
        ),
    ]