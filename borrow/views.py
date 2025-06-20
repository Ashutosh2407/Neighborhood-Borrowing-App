from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import *
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import User,Item, Group
from .serializers import UserSerizalizer,ItemSerializer, GroupSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from django.utils.timezone import now
from datetime import timedelta
# Create your views here.
def index(request):
    return HttpResponse("Hello This is homepage.")

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerizalizer
    permission_classes = [AllowAny]
    authentication_classes = []

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        user = serializer.save()
        user.set_password(password)
        user.save()

class ListCreateItemView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    
        




@csrf_exempt
@permission_classes([IsAdminUser])
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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

@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def item_borrow(request,pk):
    try:
        item = get_object_or_404(Item, pk = pk)
    except:
        return Response(status=404)
    
    if request.method == "POST":
        if item.status == "Av":
            item.borrower = request.user
            item.status = "Br"
            item.date_borrowed = now()
            item.due_date = now()+timedelta(days=14)
            item.save()
            return Response({"message":"Borrowed successfully."})
        return Response({"message":"Item Not Available."})

@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def item_return(request,pk):
    try:
        item = get_object_or_404(Item,pk=pk)
    except:
        return Response(status=404)

    if request.method == "POST":
        if item.status == "Br":
            item.borrower = None
            item.status = "Av"
            item.date_borrowed = None
            item.due_date = None
            item.save()
            return Response("Item returned successfully.")
        return Response("Item not available.")





@api_view(['GET','POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def group_list(request):

    if request.method == "GET":
        group = Group.objects.all()
        serializer = GroupSerializer(group, many =True, context = {'request':request})
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = GroupSerializer(data=request.data,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status =404)
    

@api_view(['GET','PATCH','DELETE'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def group_detail(request, pk):

    try:
        group = Group.objects.get(pk = pk)
    except:
        return Response(status =404)
    
    if request.method =="GET":
        serializer = GroupSerializer(group, context = {'request':request})
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = GroupSerializer(group, data = request.data, partial = True, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        return Response(serializer.errors, status=404)
    
    elif request.method == "DELETE":
        group.delete()
        return Response(status=200)

