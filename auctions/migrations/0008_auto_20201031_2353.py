# Generated by Django 3.1.1 on 2020-11-01 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_comment_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='current_bid',
            new_name='bid_offer',
        ),
        migrations.AddField(
            model_name='listing',
            name='current_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
