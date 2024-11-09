from django.db import models

# Create your models here.

class Vehicle(models.Model):
    
    name = models.CharField(max_length=100)
    
    varient = models.CharField(max_length=100)
    
    description = models.TextField()
    
    fuel_options = (
        ("petrol","petrol"),
        ("diesel","diesel"),
        ("EV","EV"),
        ("CNG","CNG")
    )
    
    fuel_type = models.CharField(max_length=200,choices=fuel_options,default="petrol")
    
    running_km = models.PositiveIntegerField()
    
    color = models.CharField(max_length=100)
    
    price = models.PositiveIntegerField()
    
    brand = models.CharField(max_length=100)
    
    owner_options = (
        ("single","single"),
        ("second","second"),
        ("other","other")

    )
    
    owner_type = models.CharField(max_length=100,choices=owner_options,default="single")
    
    picture = models.ImageField(upload_to="vehicle_images",null=True)

    def __str__(self):
        
        return self.name
    

    
    
    
    
