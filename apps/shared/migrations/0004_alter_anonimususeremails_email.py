# Generated by Django 5.0.3 on 2024-04-18 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_anonimususeremails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonimususeremails',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]