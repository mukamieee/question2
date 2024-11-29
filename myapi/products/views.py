from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# List and Create Products
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieve, Update, and Delete a Product
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def create(self, request, *args, **kwargs):
    # Deserialize the incoming JSON data
    serializer = self.get_serializer(data=request.data)
    
    if serializer.is_valid():  # Validate the input data
        self.perform_create(serializer)  # Save the product
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED  # Respond with 201 Created
        )
    else:
        # Respond with 400 Bad Request if data is invalid
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
