from django.contrib import admin

from .models import Bid, Comment, Listing, User, Category

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "starting_bid", "current_bid", "creator")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)

admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Listing, ListingAdmin)
admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
