# Generated by Django 3.1.1 on 2020-10-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201021_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Bio',
            field=models.TextField(max_length=300, null=True),
        ),
    ]