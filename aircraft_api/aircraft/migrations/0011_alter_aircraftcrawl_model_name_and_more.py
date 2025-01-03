# Generated by Django 5.1.1 on 2024-11-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0010_modelcrawl_last_parsed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='model_name',
            field=models.CharField(default='foo', max_length=128, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='unparsed_data',
            field=models.JSONField(default=dict),
        ),
    ]
