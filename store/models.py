from decimal import Decimal

from django.db import models


# The `Category` class defines a model with fields for name and slug, along with Meta options for
# ordering and verbose name.
class Category(models.Model):
    name = models.CharField(
        max_length=250,
        db_index=True,
        help_text="Enter Category Name",
        verbose_name="Category Name",
    )
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ("name",)
       
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


# Product Model
# The `Product` class defines a model with fields for category, title, slug, image, description,
# price, discount, and availability.
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/",default="default.png", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    discount = models.DecimalField(
        max_digits=4, decimal_places=2, default=Decimal("0.00")
    )

    available = models.BooleanField(default=True)

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "products"
        

    def __str__(self):
        return self.title
