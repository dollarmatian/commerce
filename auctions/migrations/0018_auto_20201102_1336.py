# Generated by Django 3.1.1 on 2020-11-02 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_listing_high_bidder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='high_bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_bids', to=settings.AUTH_USER_MODEL),
        ),
    ]