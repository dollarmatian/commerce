from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# listings
#    title
#    starting bid
# image url
# category enum?

class Listing(models.Model):
    title = models.CharField(max_length=120, default='')
    starting_bid = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    current_bid = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image_url = models.URLField(blank=True, default='')
    creator = models.CharField(max_length=64, default='')
    description = models.CharField(max_length=360, default='')
    category = models.CharField(max_length=16, default='Unsorted')
    # NONE = 'NA'
    # FASHION = 'FA'
    # TOYS = 'TY'
    # ELECTRONICS = 'EL'
    # HOME = 'HM'
    # YEAR_IN_SCHOOL_CHOICES = (
    # (FASHION, 'Fashion'),
    # (TOYS, 'Toys'),
    # (ELECTRONICS, 'Electronics'),
    # (HOME, 'Home'),
    # (NONE, 'None')
    # )
    # category = models.CharField(
    # max_length=2,
    # choices=YEAR_IN_SCHOOL_CHOICES,
    # default=NONE,
    # )
    def __str__(self):
        return f"{self.title}"

# bids
class Bid(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item_name")
    bid_offer = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    def __str__(self):
        return f"{self.item}, Bid By: {self.creator} for {self.bid_offer}"

# comments
class Comment(models.Model):
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comment_item_name")
    creator = models.CharField(max_length=64, default='')
    comment = models.CharField(max_length=240, default='')

    def __str__(self):
        return f"{self.item}, Comment By: {self.creator}"

#category

class Category(models.Model):
    category = models.CharField(max_length=16, default='Unsorted')