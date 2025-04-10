from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import *
from .models import User,Item
from .serializers import UserSerizalizer,ItemSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello This is homepage.")

@csrf_exempt
def user_list(request):
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerizalizer(user, many=True)
        return JsonResponse(serializer.data, safe = False)
    

@csrf_exempt
def item_list(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer_context = {'request':request,}
        serializer = ItemSerializer(items, context = serializer_context, many = True)
        return JsonResponse(serializer.data, safe= False)