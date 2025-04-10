from rest_framework import serializers
from .models import User, Item

class UserSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# class ItemSerializer(serializers.HyperlinkedModelSerializer):
    
#     owner = serializers.HyperlinkedRelatedField( read_only= True, view_name = "owner_detail")
    
    
#     class Meta:
#         model = Item
#         fields = ["url","item_id","item_name" ,"owner", "description","date_borrowed" ,"due_date" ,"created_at","status" ]
        
        
   
   

