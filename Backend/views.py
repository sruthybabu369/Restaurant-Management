from django.shortcuts import render, redirect
from Backend.models import shop_db, food_db
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def indexpage(request):
    return render(request, "index.html")
# Create your views here.
def shoppage(request):
    return render(request, "shop.html")

def display_shop(request):
    data = shop_db.objects.all()
    return render(request, "displayshop.html", {'data': data})

def save_shop(request):
    if request.method == "POST" :
        na = request.POST.get('sname')
        ow = request.POST.get('owner')
        pl = request.POST.get('place')
        di = request.POST.get('district')
        mob = request.POST.get('mobnumber')

        obj = shop_db(SName=na, OName=ow, Place=pl, District=di, Contactno=mob)
        obj.save()
        return redirect(shoppage)

def edit_shop(request, shop_id):
    data = shop_db.objects.get(id=shop_id)
    return render(request, "Editshop.html", {'data': data})

def update_shop(request, shop_id):
    if request.method == "POST":
        na = request.POST.get('sname')
        ow = request.POST.get('owner')
        pl = request.POST.get('place')
        di = request.POST.get('district')
        mob = request.POST.get('mobnumber')
        shop_db.objects.filter(id=shop_id).update(SName=na, OName=ow, Place=pl, District=di, Contactno=mob)

        return redirect(display_shop)

def delete_shop(request, shop_id):
    data = shop_db.objects.filter(id=shop_id)
    data.delete()
    return redirect(display_shop)

def foodpage(request):
    return render(request, "Food.html")

def display_food(request):
    data = food_db.objects.all()
    return render(request, "displayfood.html", {'data': data})

def save_food(request):
    if request.method == "POST" :
        na = request.POST.get('fname')
        pr = request.POST.get('price')
        qt = request.POST.get('quantity')
        des = request.POST.get('description')


        obj = food_db(FName=na, Price=pr, Quantity=qt, Description=des)
        obj.save()
        return redirect(foodpage)

def edit_food(request, food_id):
    data = food_db.objects.get(id=food_id)
    return render(request, "Editfood.html", {'data': data})

def update_food(request, food_id):
    if request.method == "POST":
        na = request.POST.get('fname')
        pr = request.POST.get('price')
        qt = request.POST.get('quantity')
        des = request.POST.get('description')
        food_db.objects.filter(id=food_id).update(FName=na, Price=pr, Quantity=qt, Description=des)

        return redirect(display_food)

def delete_food(request, food_id):
    data = food_db.objects.filter(id=food_id)
    data.delete()
    return redirect(display_food)
def admin_login(request):
    return render(request, "adminlogin.html")

def admin_page(request):
    if request.method=="POST":
       un = request.POST.get('username')
       pwd = request.POST.get('pass')
       if User.objects.filter(username__contains=un).exists():
           x = authenticate(username=un, password=pwd)
           if x is not None:
               login(request, x)
               request.session['username']=un
               request.session['password']=pwd
               return redirect(indexpage)
           else:
               return redirect(admin_login)


       else:
           return redirect(admin_login)