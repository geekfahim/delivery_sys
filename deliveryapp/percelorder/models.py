from django.db import models

# Create your models here.


class Merchant(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

def __str__(self):
        return self.city


class Percel(models.Model):
    TYPE = (
        ('Fragile','Fragile'),
        ('Liquid','Liquid'),
    )
    WEIGHT = (
        ('Fragile','Fragile'),
        ('Liquid','Liquid'),
    )
    merchant = models.ForeignKey(Merchant,null=True,on_delete=models.SET_NULL)
    product_type = models.CharField(max_length=200, null=True,choices=TYPE)
    product_weight = models.CharField(max_length=200, null=True,choices=WEIGHT)
    district= models.CharField(max_length=200,null=True)
    division= models.CharField(max_length=200,null=True)
    city= models.CharField(max_length=200,null=True)
    delivery_charge=models.FloatField(max_length=200, null=True,default=0)
    cod_charge=models.FloatField(max_length=200, null=True,default=0)
    return_charge=models.FloatField(max_length=200, null=True,default=0)
    total_cost=models.FloatField(max_length=200, null=True,default=0)
    
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.merchant