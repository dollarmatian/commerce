from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,  Listing, Comment, Category

from django import forms



class CreateForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(widget=forms.Textarea(attrs={ "style": "resize: none" })) 
    starting_bid = forms.DecimalField(max_digits=6, decimal_places=2)
    image_url = forms.URLField(required=False)

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={ "style": "resize: none", "placeholder": "Leave Comment" }),label='')

class BidForm(forms.Form):
    bid = forms.DecimalField(max_digits=6, decimal_places=2, label='')

def index(request):
    return render(request, "auctions/index.html",
     {
        "listings": Listing.objects.all()
    }
    )



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            image_url = form.cleaned_data["image_url"]
            creator = request.user
            category = request.POST["category"]
            new_item = Listing(title = title, description = description, starting_bid = starting_bid, image_url = image_url, creator = creator, category = category)

          
            new_item.save()

            
            return HttpResponseRedirect(reverse("listing",args=(title,)))

    else:
        return render(request, "auctions/create.html", {
        "form": CreateForm(),
        "categories": Category.objects.all()
        })

def listing(request, item):
    if request.user is None:
        return render(request, "auctions/listing.html", {
        "title": item,
        "listing": Listing.objects.get(title=item),
        "comments": Comment.objects.filter(item=itemSearch).all()
    })
    
    itemSearch = Listing.objects.get(title=item)
    if User.objects.get(username=request.user).listings:
        watchlist = User.objects.get(username=request.user).listings.all()


    if (itemSearch in watchlist):

        onList = True
    else:

        onList = False

    if request.method == "POST":
        form = BidForm(request.POST)

        if form.is_valid():
            bid = form.cleaned_data["bid"]
        

            if (itemSearch.starting_bid < bid) and (itemSearch.current_bid < bid):
                itemSearch.current_bid = bid
                itemSearch.high_bidder = request.user
                itemSearch.save()

                # bidder = request.user
                # new_bid = Bid(item = itemSearch, bid_offer = bid, bid_user = bidder)
                # new_bid.save()
                return HttpResponseRedirect(reverse("listing",args=(item,)))
            else:
                return render(request, "auctions/listing.html", {
                    "title": item,
                    "listing": itemSearch,
                    "onList": onList,
                    "form": CommentForm(),
                    "comments": Comment.objects.filter(item=itemSearch).all(),
                    "bidForm": form,
                    "message": "Enter Valid Bid" 
                })

    return render(request, "auctions/listing.html", {
        "title": item,
        "listing": itemSearch,
        "onList": onList,
        "form": CommentForm(),
        "comments": Comment.objects.filter(item=itemSearch).all(),
        "bidForm": BidForm()

    })


def categories(request):

    return render(request, "auctions/categories.html",{
        "categories": Category.objects.all()
    } )

def category(request, name):

    return render(request, "auctions/category.html", {
        "category": name,
        "results": Listing.objects.filter(category=name).all()
    })

def watchlist(request):
    user =  request.user
    userData = User.objects.get(username=user)
    print(userData)
    watchlist = userData.listings.all()


    return render(request, "auctions/watchlist.html", {
        "user": user,
        "watchlist": watchlist
    })

def edit_watchlist(request, listing):
    user =  request.user
    userData = User.objects.get(username=user)
    watchlist = userData.listings.all()
    edit_listing = Listing.objects.get(title=listing)

    if edit_listing not in watchlist:
        userData.listings.add(edit_listing)
    else:
        userData.listings.remove(edit_listing)
    userData.save()
    watchlist = userData.listings.all()
    return HttpResponseRedirect(reverse("watchlist"))

def commentDelete(request, item, comment):
        delete_comment = Comment(comment)
        delete_comment.delete()
        return HttpResponseRedirect(reverse("listing",args=(item,)))
    
def commentAdd(request, item):
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.cleaned_data["comment"]
            creator = request.user
            itemSearch = Listing.objects.get(title=item)
            new_comment = Comment(item = itemSearch, creator = creator, comment = comment)

            new_comment.save()
            return HttpResponseRedirect(reverse("listing",args=(item,)))


def closeListing(request, item):
    itemSearch = Listing.objects.get(title=item)

    if str(itemSearch.creator) == str(request.user.username):

        print(itemSearch.is_active)
        itemSearch.is_active = 0
        itemSearch.save()
    
    return HttpResponseRedirect(reverse("listing",args=(item,)))