from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class UserDetail(models.Model):
    
    ROLES = [
        ('farmer', 'Farmer'),
        ('supplier', 'Supplier'),
        ('wholesaler', 'Wholesaler')
    ]

    profilePic = models.ImageField(upload_to=upload_to, blank=True, null=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField()
    contacts = models.TextField()

    role = models.CharField(
        max_length = 15,
        default = 'farmer',
        choices = ROLES
    )

    def __str__(self):
        return self.username


class Product(models.Model):
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    unit_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.name
    

class VendorProduct(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    unit_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.name
    

class Order(models.Model):

    ORDER_BY = [
        ('wholesaler', 'Wholesaler'),
        ('farmer', 'Farmer')
    ]

    buyers_email = models.EmailField()
    sellers_email = models.EmailField()
    
    itemId = models.IntegerField()
    qty = models.IntegerField(default=1)

    date = models.DateTimeField(auto_now_add=True)
    order_by = models.CharField(
        max_length=15,
        default='wholesaler',
        choices=ORDER_BY
    )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Item id {self.itemId}"
