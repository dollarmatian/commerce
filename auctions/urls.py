from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listings/<str:item>", views.listing, name="listing"),
    path("listings/<str:item>/close", views.closeListing, name="close_listing"),
    path("categories", views.categories, name= "categories"),
    path("categories/<str:name>", views.category, name= "category"),
    path("watchlist", views.watchlist, name= "watchlist"),
    path("watchlist/<str:listing>", views.edit_watchlist, name= "edit_watchlist"),
    path("comments/<str:item>/<int:comment>", views.commentDelete, name="commentDelete"),
    path("comments/<str:item>", views.commentAdd, name="commentAdd"),
    

]
