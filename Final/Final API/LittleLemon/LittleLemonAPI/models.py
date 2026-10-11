from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="menu_items"
    )

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ("user","menuitem")

class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name="orders"
    )
    delivery_crew = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="delivery_orders",
        null=True,
        blank=True
    )
    status = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=8,decimal_places=2)
    date = models.DateField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,related_name="items"
    )
    menuitem = models.ForeignKey(MenuItem,on_delete=models.PROTECT)
    quantity = models.PositiveBigIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)