# Generated by Django 3.1.1 on 2020-11-02 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auto_20201102_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='high_bidder',
        ),
    ]
