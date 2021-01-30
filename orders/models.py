from django.db import models

# Create your models here.
class PizzaSize(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.size}"

class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.size}"


class PizzaBase(models.Model):

    name = models.CharField(max_length=60)
    image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name}"


class PizzaTopping(models.Model):

    topping_name = models.CharField(max_length=60)
    number_of_toppings = models.IntegerField()
    
    def __str__(self):
        return f"{self.topping_name}"

class Pizza(models.Model):

    base = models.ManyToManyField(PizzaBase, related_name="pizzatopping")
    pizza_topping = models.ForeignKey(PizzaTopping, on_delete=models.CASCADE, related_name="pizza_top")
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE, related_name="pizzasize")
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.pizza_topping} {self.size} {self.price}"

class Topping(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class SubName(models.Model):

    name = models.CharField(max_length=70)
    sub_image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name}"

class Sub(models.Model):

    name = models.ForeignKey(SubName, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="sub_size")
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.name} {self.size} ${self.price}"

class AddOn(models.Model):

    name = models.CharField(max_length=70)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"({self.name}) Price: ${self.price}"

class Pasta(models.Model):

    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    pasta_image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name} {self.price}"

class Salad(models.Model):

    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    salad_image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name} {self.price}"

class DinnerPlatterName(models.Model):
    
    name = models.CharField(max_length=20)
    dp_image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name}"  

class DinnerPlatter(models.Model):
    name = models.ForeignKey(DinnerPlatterName, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.name} {self.size} ${self.price}"

class RecivedOrders(models.Model):

    username = models.CharField(max_length=65)
    all_items = models.TextField()
    order_total = models.DecimalField(decimal_places=2, max_digits=5)
    status = models.CharField(max_length=65, default="Preparing")
    date = models.CharField(max_length=65)
    time = models.CharField(max_length=65)

    def __str__(self):
        return f"Username: {self.username}, Status: ({self.status})"

class Cart(models.Model):

    username = models.CharField(max_length=65)
    item_name = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"Username: {self.username}, Item: {self.item_name} Price: {self.price}"


