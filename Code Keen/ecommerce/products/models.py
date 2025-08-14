from django.db import models
from django.utils.text import slugify

# Create your models here.
class Catagory(models.Model):
      catagory_name = models.CharField(max_length=100)
      slug = models.SlugField(max_length=200, blank=True)

      def save(self, *args, **kwargs):
            self.slug = slugify(self.catagory_name)
            super(Catagory,self).save(*args, **kwargs)

      def __str__(self):
            return self.catagory_name

class Product(models.Model):
      category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
      product_name = models.CharField(max_length=100)
      image = models.ImageField(upload_to='static/products')
      price = models.CharField(max_length=20)
      stock = models.IntegerField(default=100)
      total_price = models.CharField(max_length=20)
      total_weight = models.CharField(max_length=20)
      description = models.TextField()

      def __str__(self):
            return str(self.category)

