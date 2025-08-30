from rest_framework import serializers
from .models import User, Item, Group

class UserSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    borrower = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), required = False)
    
    class Meta:
        model = Item
        fields = ['url','item_id','item_name','owner','description','borrower','date_borrowed','due_date','created_at','status']
        extra_kwargs = {"owner":{"read_only":True}}



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), many = True)

    class Meta:
        model = Group
        fields = ['url','group_id', 'group_name','description','city','admin','members','time_created','status']
    
    
   

