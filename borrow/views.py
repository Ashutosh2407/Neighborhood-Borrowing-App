from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User,Item,UserForm
from .serializers import UserSerizalizer

# Create your views here.
def index(request):
    return HttpResponse("Hello This is homepage.")

def create_user(request):
    if request.method == "GET":
        form = UserForm()
        return render(request,"borrow/user.html", {"form":form})


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

    

