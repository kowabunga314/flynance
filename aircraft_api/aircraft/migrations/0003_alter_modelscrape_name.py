# Generated by Django 5.1.1 on 2024-10-07 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0002_manufacturerscrape_modelscrape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelscrape',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]