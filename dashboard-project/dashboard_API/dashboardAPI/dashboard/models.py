from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    access = models.CharField(max_length=100)

class customerContats(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=100)
    registrarId = models.CharField(max_length=100)

class dataInvoice(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=100)
    date = models.DateField()
"""
class Transactions(models.Model):
    txId = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    
    def barChart(self):
        return self.amount * self.quantity
    
    def pieChart(self):
        return self.amount * self.quantity
    
    def lineChart(self):
        return self.amount * self.quantity

class geographyData(models.Model):
    id = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class geoFeatures(models.Model):
    # Primary key field, usually created automatically
    id = models.AutoField(primary_key=True)
    
    # JSONField to store the GeoJSON data
    geojson_data = models.JSONField()

    def __str__(self):
        return self.geojson_data["properties"]["name"]
"""