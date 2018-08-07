from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from foodlist.models import Category, Food

# Food List Views

def index(request):
    if not request.user.is_authenticated:
        return render(request, "foodlist/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "foodlist/home.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "foodlist/error.html", {"message": "Invalid credentials.", "backto": "login"})
    else:
        return render(request, "foodlist/login.html", {"message": None})

def register_view(request):
    if request.method == "POST":
        u_firstname = request.POST.get('firstname')
        u_lastname = request.POST.get('lastname')
        u_email = request.POST.get('email')
        u_uname = request.POST.get('username')
        u_pwd = request.POST.get('password')

        #check if user exists
        userlist = User.objects.all()
        namecheck = userlist.filter(username = u_uname)
        emailcheck = userlist.filter(email = u_email)

        if namecheck:
            return render(request, "foodlist/error.html", {"message": "Username already exists!", "backto": "register"})
        elif emailcheck:
            return render(request, "foodlist/error.html", {"message": "Email already exists!", "backto": "register"})
        else:
            newuser = User.objects.create_user(u_uname, u_email, u_pwd)
            newuser.first_name = u_firstname
            newuser.last_name = u_lastname
            newuser.save()
            return render(request, "foodlist/login.html")
    else:
        return render(request, "foodlist/register.html")


def logout_view(request):
    logout(request)
    return render(request, "foodlist/login.html")

def search_foods(request):
    if request.method == "POST":
        search_text = request.POST.get('search_text')
    else:
        search_text = ''

    food_items = Food.objects.filter(item_name__contains=search_text)

    context = {
        "search": food_items
    }

    return render(request,"ajax_search.html",context)