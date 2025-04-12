from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

class Item(models.Model):
    Statuses = {
        "Av":"Available", 
        "Re":"Requested", 
        "Br":"Borrowed", 
        "Ov":"Overdue", 
        "R":"Returned"
    }
    item_id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=50, default=None)
    owner = models.ForeignKey(User, related_name = "owner",on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    borrower = models.ForeignKey(User, related_name= "borrower",on_delete=models.SET_NULL, null=True, blank=True, default=None)
    date_borrowed = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank =True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Statuses, default="Av")

    def __str__(self):
        return self.item_name

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]