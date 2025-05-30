from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from decimal import Decimal, ROUND_HALF_UP
from SysAdmin.models import WebUsers

# Service model
class service(models.Model):
    service_image = models.FileField(upload_to='food/', max_length=250, null=True, default="/food/set-vector.jpg")
    service_title = models.CharField(max_length=50)
    service_price = models.IntegerField(null=True, default=None)
    service_oldprice = models.IntegerField(null=True, default=0, blank=True)
    service_rating = models.CharField(max_length=20, null=True, default="100", blank=True)
    service_badge = models.CharField(max_length=20, null=True, default="Amazon's Choice", blank=True)
    service_desc = HTMLField(blank=True)
    menu_slug = AutoSlugField(populate_from='service_title', unique=True, null=True, default=None)
    service_deal = models.IntegerField(null=True, default=20, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.service_title or "Unnamed Service"

    def save(self, *args, **kwargs):
        if self.service_oldprice and self.service_price:
            discount_val = (1 - (self.service_price / self.service_oldprice)) * 100
            self.discount = Decimal(discount_val).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        super().save(*args, **kwargs)


# Cart model

class Cart(models.Model):
    cart_user = models.ForeignKey(WebUsers, on_delete=models.CASCADE, related_name='cart_items')
    item_title = models.CharField(max_length=50, blank=True, null=True)
    item_price = models.IntegerField(blank=True, null=True)
    item_rating = models.CharField(max_length=20, default="100", blank=True, null=True)
    item_image = models.FileField(upload_to='food/', max_length=250, blank=True, null=True, default=None)
    item_quantity = models.PositiveIntegerField(default=1)
    item_slug = AutoSlugField(populate_from='item_title', unique=True, null=True, default=None)

    def __str__(self):
        return self.item_title or "Cart Item"




# Main Page model
class mainpage(models.Model):
    mainpage_image = models.FileField(upload_to='mainpage/', max_length=250, null=True, default="/mainpage/set-vector.jpg")
    mainpage_title = models.CharField(max_length=50)
    mainpage_desc = HTMLField()
    mainpage_slug = AutoSlugField(populate_from='mainpage_title', unique=True, null=True, default=None)

    def __str__(self):
        return self.mainpage_title or "Main Page"
