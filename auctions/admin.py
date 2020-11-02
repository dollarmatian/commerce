from django.contrib import admin

from .models import  Comment, Listing, User, Category

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "starting_bid", "current_bid", "creator", "is_active")
    # filter_horizontal = ("comment")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ("listings",)

# admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Listing, ListingAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
