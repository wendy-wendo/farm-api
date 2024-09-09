from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import UserDetailSerializer, ProductSerializer, VendorProductSerializer, OrderSerializer
from .models import UserDetail, Product, VendorProduct, Order

# Create your views here.
@api_view(['GET'])
def index(request):
    apiUrls = {
        'UsersList': '/users-list/',
        'User': '/user/<str:pk>/',
        'Create User': '/user-create/',
        'Update User': '/update-user/'
    }

    return Response(apiUrls)


@api_view(['GET'])
def users(request):
    user_details = UserDetail.objects.all()
    serializer = UserDetailSerializer(user_details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user(request, email):
    user_detail = UserDetail.objects.get(email=email)
    serializer = UserDetailSerializer(user_detail, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
    parser_classes = (MultiPartParser, FormParser)
    
    serializer = UserDetailSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def userUpdate(request, pk):
    parser_classes = (MultiPartParser, FormParser)

    user_detail = UserDetail.objects.get(id=pk)
    serializer = UserDetailSerializer(instance=user_detail, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
    parser_classes = (MultiPartParser, FormParser)
    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def specificProducts(request, email):
    products = Product.objects.filter(email=email)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response("Product successfully deleted!")


@api_view(['GET'])
def vendorProducts(request):
    vendorProducts = VendorProduct.objects.all()
    serializer = VendorProductSerializer(vendorProducts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def vendorProduct(request, pk):
    vendorProduct = VendorProduct.objects.get(id=pk)
    serializer = VendorProductSerializer(vendorProduct, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def specificVendorProducts(request, email):
    vendorProducts = VendorProduct.objects.filter(email=email)
    serializer = VendorProductSerializer(vendorProducts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def vendorProductCreate(request):
    parser_classes = (MultiPartParser, FormParser)
    
    serializer = VendorProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def vendorProductUpdate(request, pk):
    parser_classes = (MultiPartParser, FormParser)

    vendorProduct = VendorProduct.objects.get(id=pk)

    serializer = VendorProductSerializer(instance=vendorProduct, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def order(request, pk):
    order = Order.objects.get(id = pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data) 


@api_view(['POST'])
def orderCreate(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def orderUpdate(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
