# Generated by Django 3.1.1 on 2020-10-21 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.profile'),
        ),
    ]