# Generated by Django 3.1.1 on 2020-11-02 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_delete_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
    ]
