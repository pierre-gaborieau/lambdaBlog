# Generated by Django 3.1.1 on 2020-10-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Bio',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
