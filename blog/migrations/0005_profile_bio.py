# Generated by Django 3.1.1 on 2020-10-21 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201021_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Bio',
            field=models.TextField(null=True),
        ),
    ]
