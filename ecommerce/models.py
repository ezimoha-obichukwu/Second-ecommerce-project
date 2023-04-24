from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ("Men", "Men"),
    ("Women", "Women"),
    ("General", "General")
)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images", default="product.jpg")

    # class Meta:
    #     verbose_name_plural = 'Producties' To change the plural form of the model in the admin panel

    def __str__(self):
        return self.name