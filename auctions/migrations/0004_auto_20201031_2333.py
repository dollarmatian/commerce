# Generated by Django 3.1.1 on 2020-11-01 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201031_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='creator',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
