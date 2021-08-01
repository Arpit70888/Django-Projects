import re
from django.shortcuts import render
from rest_framework import serializers
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response, responses
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ShowOne(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product,many = False)
    return Response(serializer.data)

@api_view(['POST'])
def insertProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def UpdateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Product Deleted successfully')

