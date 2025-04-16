from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User,Item, Group
from .serializers import UserSerizalizer,ItemSerializer, GroupSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello This is homepage.")

@csrf_exempt
@api_view(["GET","POST"])
def user_list(request):
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerizalizer(user, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = UserSerizalizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

@api_view(["GET","PUT","DELETE"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk = pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = UserSerizalizer(user)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = UserSerizalizer(user,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 404)
    
    elif request.method == "DELETE":
        user.delete()
        return Response(status = 204)


@csrf_exempt
@api_view(['GET','POST'])
def item_list(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer = ItemSerializer(items,many = True, context = {'request':request})
        return Response(serializer.data, status=200)
    
    elif request.method == 'POST':
        serializer = ItemSerializer(data = request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
    
@csrf_exempt
@api_view(['GET','PATCH','DELETE'])
def item_detail(request,pk):
    try:
        item = get_object_or_404(Item, pk = pk)
    except:
        return Response(status =404)
    
    serializer = ItemSerializer(item, context = {'request':request})
    
    if request.method == "GET":
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = ItemSerializer(item, data = request.data,partial = True, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors, status = 404)
    
    elif request.method == "DELETE":
        item.delete()
        return Response(status = 200)


@api_view(['GET','POST'])
@csrf_exempt
def group_list(request):
    if request.method == "GET":
        group = Group.objects.all()
        serializer = GroupSerializer(group, many =True, context = {'request':request})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = GroupSerializer(data= request.data,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status =404)
    

@api_view(['GET','PATCH','DELETE'])
@csrf_exempt
def group_detail(request, pk):
    try:
        group = Group.objects.get(pk = pk)
    except:
        return Response(status =404)
    
    if request.method =="GET":
        serializer = GroupSerializer(group, context = {'request':request})
        return Response(serializer.data)

