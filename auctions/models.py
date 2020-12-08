from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    listings = models.ManyToManyField('Listing', related_name='watchlist_items', blank=True)

class Listing(models.Model):
    title = models.CharField(max_length=120, default='')
    starting_bid = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    current_bid = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    creator = models.CharField(max_length=64, default='')
    high_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items_winning", default='', null=True)
    image_url = models.URLField(blank=True, default='')
    is_active = models.IntegerField(default=1,)
    description = models.CharField(max_length=360, default='')
    category = models.CharField(max_length=16, default='Unsorted')


    def __str__(self):
        return f"{self.title}"

# bids
# class Bid(models.Model):
#     item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item_name")
#     bid_offer = models.DecimalField(max_digits=6, decimal_places=2, default=0)
#     bid_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items_bid", default='')
#     def __str__(self):
#         return f"{self.item}, Bid By: {self.creator} for {self.bid_offer}"

# comments
class Comment(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comment_item_name")
    creator = models.CharField(max_length=64, default='')
    comment = models.CharField(max_length=240, default='')

    def __str__(self):
        return f"{self.item}, By: {self.creator}"

#category

class Category(models.Model):
    category = models.CharField(max_length=16, default='Unsorted')
