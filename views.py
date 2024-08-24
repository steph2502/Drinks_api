from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])

def drinks_list(request,format=None):

    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = DrinkSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status= status.HTTP_201_CREATED)


@api_view(['GET','PuT','DELETE'])

def drinks_detail(request,id,format=None):
    try:
        drinks = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DrinkSerializer(drinks)
        return Response(serializer.data)

    elif request.method == "PUT":
         serializer = DrinkSerializer(drinks,data= request.data)
         if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status= status.HTTP_201_CREATED)
         else:
            return Response( serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method =="DELETE":
        drinks.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

