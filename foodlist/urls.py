from django.urls import path

from . import views

# users urls
urlpatterns = [
    path("", views.landing, name="landing"),
    path("home", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("new_list", views.new_list, name="new_list"),
    path("get_foods/", views.get_foods, name='get_foods'),
    path("get_ldetail/", views.get_ldetail, name='get_ldetail')
]
