from .models import Drinks
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def showdrinks(request):
    if request.method == 'GET':
        all_drinks = Drinks.objects.all()
        serializer = DrinkSerializer(all_drinks, many=True)
        return JsonResponse({'drinks': serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])

def get_drink(request, id):

    try:
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
        pass
    elif request.method == "POST":
        pass



