from rest_framework import serializers
from .models import User, Item, Group

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


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), many = True)

    class Meta:
        model = Group
        fields = ['url','group_id', 'group_name','description','city','admin','members','time_created','status']
    
    
   

