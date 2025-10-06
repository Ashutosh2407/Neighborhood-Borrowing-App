from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Item(models.Model):
    Statuses = {
        "Available":"Available", 
        "Requested":"Requested", 
        "Borrowed":"Borrowed", 
        "Overdue":"Overdue", 
        "Returned":"Returned"
    }
    item_id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, related_name = "owner",on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    borrower = models.ForeignKey(User, related_name= "borrower",on_delete=models.SET_NULL, null=True, blank=True, default=None)
    date_borrowed = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank =True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Statuses, default="Available")

    def __str__(self):
        return self.item_name

class Group(models.Model):
    status = {
        "A": "active",
        "I": "inactive",
        "D":"Dead"
    }
    group_id = models.BigAutoField(primary_key=True)
    group_name = models.CharField(max_length=50, null= True, default=None, blank = False)
    description = models.CharField(max_length=200, null= True, default=None)
    city = models.CharField(max_length=20,null= True,default=None)
    admin = models.ForeignKey(User, related_name="admin",null=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(User)
    time_created = models.DateTimeField(default = timezone.now)
    status = models.CharField(choices = status, max_length=3, default = "A")

    def __str__(self):
        return f'{self.group_name} is in {self.status} state.'