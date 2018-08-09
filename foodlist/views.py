from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from foodlist.models import Category, Food, Userlist, Listdetail
import json

#Main Page
def landing(request):
    return render(request, "foodlist/landing.html")

#User Home
def index(request):
    if not request.user.is_authenticated:
        return render(request, "foodlist/login.html", {"message": None})
    else:
        user_lists = Userlist.objects.filter(user=request.user.id)

    context = {
        "user": request.user,
        "user_data": user_lists
    }
    return render(request, "foodlist/home.html", context)

#AJAX Get List Details
def get_ldetail(request):
    if request.is_ajax():
        list_no = request.GET.get('targetlist')

        userlist_det = Listdetail.objects.filter(ldetail=list_no)

        results = []
        for pl in userlist_det:
            userlist_det_json = {
                "item": f"{pl.item}",
                "category": f"{pl.item.category_id}"
            }
            results.append(userlist_det_json)
            data = json.dumps(results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


#User Login
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

#User Registration
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

#User Logout
def logout_view(request):
    logout(request)
    return render(request, "foodlist/login.html")


#Add List
def new_list(request):
    if not request.user.is_authenticated:
        return render(request, "foodlist/login.html", {"message": None})
    else:
        if request.method == "POST":
            newName = request.POST.get('userlistinput')
            fselected = inputs = request.POST.getlist('ebb[]')

            #Create New User List
            newList = Userlist(list_name=newName,user=request.user)
            newList.save()
            #get new primary key
            newPK = newList.id

            #Add Records to List Detail
            for i in fselected:
                newDets = Listdetail(ldetail=Userlist.objects.get(pk=newPK),item=Food.objects.get(pk=i))
                newDets.save()

            user_lists = Userlist.objects.filter(user=request.user.id)
            context = {
                "user": request.user,
                "user_data": user_lists
            }

            return render(request, "foodlist/home.html",context)
        else:
            food_cat = Category.objects.all()
            food_cat = food_cat.extra(order_by = ['category_name'])

            context = {
                "cg_data": food_cat
            }
            return render(request, "foodlist/new_list.html",context)

#AJAX Search Foods
def get_foods(request):
    if request.is_ajax():
        c = request.GET.get('category')
        q = request.GET.get('term')

        foods = Food.objects.filter(category_id=c)
        foods = foods.filter(item_name__icontains=q)
        foods = foods.extra(order_by = ['item_name'])

        results = []
        for pl in foods:
            foods_json = {
                "id": f"{pl.id}",
                "name": f"{pl.item_name}"
            }
            results.append(foods_json)
            data = json.dumps(results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)