from rest_framework import serializers
from .models import User, Item

class UserSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



        
        
   
   

