from django.db import models

# Create your models here.
from django.db import models

# CarItem table will have two foreign key
# 1. Product id
from mainapp.models import Product

# 2. User id
from django.contrib.auth.models import User

# Create your models here.

# Let's model a CarItem

class CartItem(models.Model):
    # 1. Product to CarItem has a one  to many  key relationship, this is represented by a foreign constraint
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Above, the 'on_delete = models.CASCADE' will ensure that all cartitems are deleted when a related Product
    # is deleted

    # 2. User to CartItem has a one to many relationship, again reperesented by a foreign key constraint
    # Here also, We ensure that a cartitem is deleted automatically if tyhe user is deleted from the website.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 3. Quantity of the specific item in cart
    quantity = models.PositiveIntegerField(default=1)

    # 4. Date when the product was added to cart
    date_added = models.DateField(auto_now_add=True)

    # string representation of CarItem object
    def _str_(self):
        return f"Product: {self.product.name} - Count: {self.quantity}"

    # method to find total price of particular item in cart
    def get_total_price(self):
        return self.quantity * self.product.price