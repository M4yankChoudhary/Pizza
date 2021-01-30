from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration", views.registration_view, name="registration"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("error", views.error, name="error"),
    path("pizza/<int:pizza_id>", views.pizza, name="pizza"),
    path("price/<int:pizza_id>/<slug:size>/<int:topping>", views.price, name="price"),
    path("subsprice/<int:sub_id>/<slug:size>", views.sub_price, name="subprice"),
    path("subs/<int:sub_id>", views.subs, name="subs"),
    path("pasta/<int:pasta_id>", views.pasta, name="pasta"),
    path("salad/<int:salad_id>", views.salad, name="salad"),
    path("pastaprice/<int:pasta_id>", views.pasta_price, name="pastaprice"),
    path("saladprice/<int:salad_id>", views.salad_price, name="saladprice"),
    path("dinnerplatters/price/<int:dp_id>/<slug:size>", views.platters_price, name="platter_price"),
    path("pizzahandler", views.pizzaHandler, name="pizzaHandler"),
    path("dinnerplatters/<int:dp_id>", views.dinner_platters, name="dinner_platters"),
    path("subshandler/<slug:sub_id>/<slug:size>", views.subsHandler, name="subshandler"),
    path("saladhandler", views.saladHandler, name="saladhandler"),
    path("pastahandler", views.pastaHandler, name="pastaHandler"),
    path("plattershandler", views.dinnerPlattersHandler, name="platterHandler"),
    path("clearcart", views.clearCart, name="clearcart"),
    path("removeItem/<int:item_id>", views.removeItem, name="removeItem"),
    path("proceed", views.proceedToBuy, name="proceed"),
    path("myorders", views.myOrders, name="myOrders"),
    path("placeorder", views.placeOrder, name="placeOrder"),
]
