# Generated by Django 4.0.3 on 2022-03-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_remove_comment_date_of_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_of_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
