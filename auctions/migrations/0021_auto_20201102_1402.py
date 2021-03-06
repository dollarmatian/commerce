# Generated by Django 3.1.1 on 2020-11-02 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_listing_high_bidder'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='items_bid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='high_bidder',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='items_winning', to=settings.AUTH_USER_MODEL),
        ),
    ]
