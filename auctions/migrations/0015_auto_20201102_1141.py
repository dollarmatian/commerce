# Generated by Django 3.1.1 on 2020-11-02 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20201101_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='creator',
            new_name='author',
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]