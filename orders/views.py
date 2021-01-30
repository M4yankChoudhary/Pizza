from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from time import localtime, strftime
import re

from .models import PizzaBase, PizzaTopping, PizzaSize, Topping, SubName, Sub, Size, AddOn, Pasta, DinnerPlatterName, DinnerPlatter, RecivedOrders, Salad, RecivedOrders, Cart

# Create your views here.
def index(request):

    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})

    total_value = 0
    cart_items = Cart.objects.filter(username__exact=request.user.username)

    for price in cart_items:
        total_value = total_value + price.price

    context = {
        "user" : request.user,
        "pizzas" : PizzaBase.objects.all(),
        "subs" : SubName.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "platters": DinnerPlatterName.objects.all(),
        "cart" : cart_items,
        "total" : total_value,
    }
    return render(request, "orders/index.html", context)

def registration_view(request):
    
    if request.method == 'GET':    
        logout(request)
        return render(request, "orders/registration.html")
    else:

        firstName = request.POST["first"]
        if not firstName:
            return render(request, "orders/registration.html", {"message": "First name required"})
        lastName = request.POST["last"]
        if not lastName:
            return render(request, "orders/registration.html", {"message": "Last name required"})
        username = request.POST["username"]
        if not username:
            return render(request, "orders/registration.html", {"message": "username required"})
        email = request.POST["email"]
        if not email:
            return render(request, "orders/registration.html", {"message": "Email required"})
        password = request.POST["password"]
        if not password:
            return render(request, "orders/registration.html", {"message": "Password required"})
        if len(password) < 8:
            return render(request, "orders/registration.html", {"message": "Make sure your password have at least 8 letters."})
        elif re.search('[0-9]',password) is None:
            return render(request, "orders/registration.html", {"message": "Make sure your password has a number in it."})
        elif re.search('[A-Z]',password) is None:
            return render(request, "orders/registration.html", {"message": "Make sure your password has a capital letter in it."})
        try:
            user = User.objects.create_user(username, email, password, first_name=firstName, last_name=lastName)
            user.save()
        except IntegrityError:
            return render(request, "orders/registration.html", {"message": "Username Already Taken."})
        return HttpResponseRedirect(reverse("index"))

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def pizza(request, pizza_id):

    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})
    
    try:
        pizza = PizzaBase.objects.get(pk=pizza_id)
        cart_items = Cart.objects.filter(username__exact=request.user.username)
    except PizzaBase.DoesNotExist:
        raise Http404("Pizza Does Not Exist")
    except Cart.DoesNotExist:
        raise Http404("Cart Error")

    size = request.GET.get("size")

    total_value = 0
    for price in cart_items:
        total_value = total_value + price.price

    context = {
        "pizza" : pizza,
        "pizzaprice" : pizza.pizzatopping.filter(pizza_topping__topping_name__icontains="Cheese", size__size__icontains="Small"),
        "pizzasizes" : PizzaSize.objects.all(),
        "pizzatoppings" : PizzaTopping.objects.all(),
        "toppings" : Topping.objects.all(),
        "cart" : Cart.objects.filter(username__exact=request.user.username),
        "total": total_value,
    }

    return render(request, "orders/pizza.html", context)

def subs(request, sub_id):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})

    try:
        sub = SubName.objects.get(pk=sub_id)
        cart_items = Cart.objects.filter(username__exact=request.user.username)
    except SubName.DoesNotExist:
        raise Http404("Sub Not Found")
    except Cart.DoesNotExist:
        raise Http404("Cart Error")

    total_value = 0
    for price in cart_items:
        total_value = total_value + price.price

    context = {
        "sizes" : Size.objects.all(),
        "sub" : sub,
        "addons": AddOn.objects.all(),
        "cart" : Cart.objects.filter(username__exact=request.user.username),
        "total": total_value,
    }

    return render(request, "orders/subs.html", context)


def pasta(request, pasta_id):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})

    try:
        pasta = Pasta.objects.get(pk=pasta_id)
        cart_items = Cart.objects.filter(username__exact=request.user.username)
    except Pasta.DoesNotExist:
        raise Http404("Pasta Not Found")
    except Cart.DoesNotExist:
        raise Http404("Cart Error")

    total_value = 0
    for price in cart_items:
        total_value = total_value + price.price

    context = {
        "pasta" : pasta,
        "cart" : Cart.objects.filter(username__exact=request.user.username),
        "total": total_value,
    }

    return render(request, "orders/pasta.html", context)

def salad(request, salad_id):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})

    try:
        salad = Salad.objects.get(pk=salad_id)
        cart_items = Cart.objects.filter(username__exact=request.user.username)
    except Salad.DoesNotExist:
        raise Http404("salad Not Found")
    except Cart.DoesNotExist:
        raise Http404("Cart Error")

    total_value = 0
    for price in cart_items:
        total_value = total_value + price.price

    context = {
        "salad" : salad,
        "cart" : Cart.objects.filter(username__exact=request.user.username),
        "total": total_value,
    }

    return render(request, "orders/salads.html", context)

def dinner_platters(request, dp_id):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})

    try:
        dinner_platter = DinnerPlatterName.objects.get(pk=dp_id)
        cart_items = Cart.objects.filter(username__exact=request.user.username)
    except Salad.DoesNotExist:
        raise Http404("Dinner Platter Not Found")
    except Cart.DoesNotExist:
        raise Http404("Cart Error")

    total_value = 0
    for price in cart_items:
        total_value = total_value + price.price

    context = {
        "sizes" : Size.objects.all(),
        "platter" : dinner_platter,
        "cart" : Cart.objects.filter(username__exact=request.user.username),
        "total": total_value,
    }

    return render(request, "orders/dinner_platters.html", context)


def price(request, pizza_id, size, topping):

    if request.method == 'POST':
        try:
            pizza = PizzaBase.objects.get(pk=pizza_id)
            p_topping = PizzaTopping.objects.get(pk=topping)
            prices = pizza.pizzatopping.filter(pizza_topping__topping_name__icontains=p_topping, size__size__icontains=size)

            for price in prices:
                pass
        
        except PizzaBase.DoesNotExist:
            raise Http404("Pizza Does Not Exist")
        return HttpResponse(f"${price.price}")
    else:
        return render(request, "orders/error.html")

def sub_price(request, sub_id, size):

    if request.method == 'POST':
        try:
            sub = SubName.objects.get(pk=sub_id)
            sub_size = Size.objects.get(size__iexact=size)
            item_price = Sub.objects.get(name__name__iexact=sub, size__size__icontains=sub_size)    
        except SubName.DoesNotExist:
            raise Http404("Sub not found")
        except Sub.DoesNotExist:
            raise Http404("Size not available")

        return HttpResponse(f"{item_price.price}")
    else:
        return render(request, "orders/error.html")

def pasta_price(request, pasta_id):

    if request.method == 'POST':
        try:
            pasta = Pasta.objects.get(pk=pasta_id)
        except Pasta.DoesNotExist:
            raise Http404("Pasta not found")
        return HttpResponse(f"{pasta.price}")
    else:
        return render(request, "orders/error.html")

def salad_price(request, salad_id):

    if request.method == 'POST':
        try:
            salad = Salad.objects.get(pk=salad_id)
        except Salad.DoesNotExist:
            raise Http404("Sub not found")
        return HttpResponse(f"{salad.price}")
    else:
        return render(request, "orders/error.html")

def platters_price(request, dp_id, size):

    if request.method == 'POST':
        try:
            platter = DinnerPlatterName.objects.get(pk=dp_id)
            item_price = DinnerPlatter.objects.get(name__name__iexact=platter, size__size__icontains=size)    
        except DinnerPlatter.DoesNotExist:
            raise Http404("Platter not found")
        except Size.DoesNotExist:
            raise Http404("Size not available")

        return HttpResponse(f"{item_price.price}")
    else:
        return render(request, "orders/error.html")

def pizzaHandler(request):
    
    if request.method == 'POST':
        try:
            user = request.user.username
            pizza_id = request.POST['id']
            pizza_name = PizzaBase.objects.get(pk=pizza_id)
            size = request.POST['size']
            p_topping = request.POST['topping']
            selected_toppings = request.POST['toppings']
            topping = PizzaTopping.objects.get(pk=p_topping)
            prices = pizza_name.pizzatopping.filter(pizza_topping__topping_name__icontains=topping, size__size__icontains=size)

            for item_price in prices:
                pass
            
        except PizzaBase.DoesNotExist:
            raise HttpResponse("Pizza Does not exist")
        except PizzaTopping.DoesNotExist:
            raise HttpResponse("Error while selecting toppings")

        if selected_toppings == "":
            items = f"{pizza_name}" + f" ({size})" + f" {topping} " + f" {selected_toppings}"
        else:
            items = f"{pizza_name}" + f" ({size})" + f" ({topping}): " + f" {selected_toppings}"
        cart = Cart(username=user, item_name=items, price=item_price.price)
        cart.save()

    return HttpResponseRedirect(reverse("pizza", args=(pizza_id,)))

def subsHandler(request, sub_id, size):

    if request.method == 'POST':
        
        try:
            user = request.user.username
            sub_name = SubName.objects.get(pk=sub_id)
            sub = Sub.objects.get(name__name__iexact=sub_name, size__size__iexact=size)
        except SubName.DoesNotExist:
            raise Http404("Sub Not Found")
        except Sub.DoesNotExist:
            raise Http404("Problem while getting the price of the selected sub")
                
        selected_add_ons = request.POST.getlist('items[]')
        total = 0
        for name in selected_add_ons:
            if selected_add_ons == []:
                pass
            else:
                addon_price = AddOn.objects.get(name__iexact=name)
                total = total + addon_price.price

        if selected_add_ons == []:
            item = f" Sub: {sub_name}" + f" ({size})" + f" {', '.join(selected_add_ons)}"
        else:
            item = f" Sub: {sub_name}" + f" ({size})" + f" with {', '.join(selected_add_ons)}"

        final_price = total + sub.price
        cart = Cart(username=user, item_name=item, price=final_price)
        cart.save()

        return HttpResponseRedirect(reverse("subs", args=(sub_id,)))

def pastaHandler(request):
    
    if request.method == 'POST':
        try:
            user = request.user.username
            pasta_id = request.POST['id']
            pasta = Pasta.objects.get(pk=pasta_id)
        except Pasta.DoesNotExist:
            raise HttpResponse("Pizza Does not exist")

        cart = Cart(username=user, item_name=f" Pasta: {pasta.name}", price=pasta.price)
        cart.save()

    return HttpResponseRedirect(reverse("pasta", args=(pasta_id,)))

def saladHandler(request):
    
    if request.method == 'POST':
        try:
            user = request.user.username
            salad_id = request.POST['id']
            if not salad_id:
                return render(request, "orders/error.html", {"message": "Invalid Selections"})
            salad = Salad.objects.get(pk=salad_id)
        except Salad.DoesNotExist:
            raise HttpResponse("Salad Does not exist")

        cart = Cart(username=user, item_name=f" Salad:{salad.name}", price=salad.price)
        cart.save()
    return HttpResponseRedirect(reverse("salad", args=(salad_id,)))

def dinnerPlattersHandler(request):
    
    if request.method == 'POST':
        try:
            user = request.user.username
            dp_id = request.POST['id']
            dp_name = DinnerPlatterName.objects.get(pk=dp_id)
            size = request.POST['size']
            item_price = DinnerPlatter.objects.get(name__name__iexact=dp_name, size__size__iexact=size)
        except DinnerPlatterName.DoesNotExist:
            raise HttpResponse("Does not exist")
        except DinnerPlatter.DoesNotExist:
            raise HttpResponse("Error while getting price")

        item = f" Dinner Platter:{dp_name} {size}"
            
        cart = Cart(username=user, item_name=item, price=item_price.price)
        cart.save()

    return HttpResponseRedirect(reverse("dinner_platters", args=(dp_id,)))

def proceedToBuy(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})
    
    total_value = 0
    cart_items = Cart.objects.filter(username__exact=request.user.username)

    for price in cart_items:
        total_value = total_value + price.price
    
    context ={
        "items": cart_items,
        "total": total_value,
        "cart" : Cart.objects.filter(username__exact=request.user.username),
    }

    return render(request, "orders/place_order.html", context)

def myOrders(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})

    context = {
        "orders": RecivedOrders.objects.filter(username__exact=request.user.username),
    }
    return render(request, "orders/my_orders.html", context)

def placeOrder(request):
    

    if request.method == 'POST':
        user = request.user.username
        total_value = 0
        cart_items = Cart.objects.filter(username__exact=request.user.username)
        

        for price in cart_items:
            total_value = total_value + price.price

        selected_items = request.POST.getlist('items[]')
        s = ', '.join(selected_items)
        recived_order = RecivedOrders(username=user, all_items=s, order_total=total_value, status="Preparing...", date=strftime(" %a, %d %b %Y", localtime()), time=strftime(" %I:%M %p", localtime()) )
        recived_order.save()
        Cart.objects.filter(username=user).delete()
        
    return render(request, "orders/thank_you.html")

def error(request):
    return render(request, "orders/error.html", {"message": "Invalid Selections"})

def clearCart(request):
    user = request.user.username
    Cart.objects.filter(username=user).delete()
    return HttpResponseRedirect(reverse("index"))

def removeItem(request, item_id):
    user = request.user.username
    Cart.objects.get(pk=item_id).delete()
    return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})