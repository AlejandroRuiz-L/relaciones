from django.db import models
from datetime import date

# Create your models here.

class Customers(models.Model):
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  age = models.SmallIntegerField()

class Employees(models.Model):
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  age = models.SmallIntegerField()
  dni = models.BigIntegerField()

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

class Reporter(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

class Article(models.Model):
  reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
  headline = models.TextField(max_length=500)
  date = models.DateField(default=date.today)

  def __str__(self):
    return self.headline
  
  class Meta:
    ordering = ['headline']
