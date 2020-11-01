from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Bid, Listing, Comment, Category

from django import forms



class CreateForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(widget=forms.Textarea(attrs={ "style": "resize: none" })) 
    starting_bid = forms.DecimalField(max_digits=6, decimal_places=2)
    image_url = forms.URLField(required=False)

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

            print(category)
            new_item.save()

            
            return HttpResponseRedirect(reverse("listing",args=(title,)))

    else:
        return render(request, "auctions/create.html", {
        "form": CreateForm(),
        "categories": Category.objects.all()
        })

def listing(request, item):


    return render(request, "auctions/listing.html", {
        "title": item,
        "listing": Listing.objects.get(title=item)
    })