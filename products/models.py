from django.db import models

class Product(models.Model):
    product_name=models.CharField(max_length=100, unique=True)
    product_brand=models.CharField(max_length=100)
    product_category=models.CharField(max_length=100)
    product_price=models.DecimalField(max_digits=10, decimal_places=2)
    skin_type=models.CharField(max_length=100)

    def __str__(self):
        return self.product_name
    
class Ingredient(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingredients')
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} in ({self.product.product_name})"
    
class Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating=models.IntegerField()
    review_text=models.TextField()
    review_date=models.DateTimeField()
    user_skin_type=models.CharField(max_length=100)

    def __str__(self):
         return f"{self.product.product_name} - {self.rating}★"

