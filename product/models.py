from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.shortcuts import reverse
# Create your models here.

class Product(models.Model):

#    CONDITION_TYPE = (
#        ("New" , "New")
#        ("Used" , "Used")
#        ("Fresh" , "Fresh")
#        ("Old" , "Old")
#        ("Ripe" , "Ripe")
#        ("Unripe" , "Unripe")
#    ) 

    # All the products information
    name = models.CharField(max_length=90)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    overview = models.TextField(max_length=10000 , default='Enter product overview')
    specification = models.TextField(max_length=8000 , default='Enter product specifications')
#    condition = models.CharField(max_length=100 , choices=CONDITION_TYPE)
    condition = models.CharField(max_length=20)
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    brand = models.ForeignKey('Brand' , on_delete=models.SET_NULL , max_length=20, null=True)
    discount_price = models.IntegerField( default='', blank=True, null=True)
    price = models.IntegerField(default='',)
    per = models.CharField(max_length=20 , null=True , default='Enter measurement unit')
    image =  models.ImageField(upload_to='main_product/' , blank=True , null=True)
    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True , null=True)


    def save(self , *args , **kwargs):
        if not self.slug and self.name :
                self.slug = slugify(self.name)
        super(Product , self).save(*args , **kwargs)

    class Meta:
            verbose_name = 'product'
            verbose_name_plural = 'products'

    def __str__(self):
        return self.name



    def get_add_to_cart_url(self):
        return reverse("cart:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("cart:remove-from-cart", kwargs={
            'slug': self.slug
        })


class ProductImages(models.Model):
   ## for product image
   product = models.ForeignKey(Product , on_delete=models.CASCADE)
   image =  models.ImageField(upload_to='products/' , blank=True , null=True)

   class Meta:
            verbose_name = 'product image'
            verbose_name_plural = 'product images'

   def __str__(self):
        return self.product.name


class Category(models.Model):
   ## for product category
   category_name = models.CharField(max_length=50)
   image = models.ImageField(upload_to='category/' , blank=True , null=True)

   slug = models.SlugField(blank=True , null=True)


   def save(self , *args , **kwargs):
        if not self.slug and self.category_name :
                self.slug = slugify(self.category_name)
        super(Category , self).save(*args , **kwargs)

   class Meta:
           verbose_name = 'category'
           verbose_name_plural = 'categories'

   def __str__(self):
        return self.category_name


class Brand(models.Model):
   ## for product brand
   brand_name = models.CharField(max_length=50)
   
   class Meta:
           verbose_name = 'brand'
           verbose_name_plural = 'brands'

   def __str__(self):
        return self.brand_name







