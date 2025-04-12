from rest_framework import serializers
from .models import User, Item

class UserSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    borrower = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), required = False)
    class Meta:
        model = Item
        fields = ['url','item_id','item_name','owner','description','borrower','date_borrowed','due_date','created_at','status']


   
   

