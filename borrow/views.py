from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import *
from .models import User,Item
from .serializers import UserSerizalizer

# Create your views here.
def index(request):
    return HttpResponse("Hello This is homepage.")

@csrf_exempt
def user_list(request):
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerizalizer(user, many=True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == "POST":
        data = JSONParser.parse(request)
        serializer = UserSerizalizer(data = data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

def user_detail(request, pk):
    try:
        user = User.objects.get(pk = pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = UserSerizalizer(user)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UserSerizalizer(user,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status = 404)
    
    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(status = 204)

    

@csrf_exempt
def item_list(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer_context = {'request':request,}
        serializer = ItemSerializer(items, context = serializer_context, many = True)
        return JsonResponse(serializer.data, safe= False)