from django.contrib import admin

# Register your models here.

from .models import Pizza, PizzaBase, PizzaSize, PizzaTopping, Topping, SubName, Size, Sub, AddOn, Pasta, Salad, DinnerPlatterName, DinnerPlatter, Cart, RecivedOrders

admin.site.register(PizzaBase)
admin.site.register(PizzaSize)
admin.site.register(PizzaTopping)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(SubName)
admin.site.register(Size)
admin.site.register(AddOn)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatterName)
admin.site.register(DinnerPlatter)
admin.site.register(Cart)
admin.site.register(RecivedOrders)