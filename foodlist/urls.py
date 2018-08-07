from django.urls import path

from . import views

# users urls
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("search", views.search_foods, name="search_foods")
]
