from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "api"
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('user/<str:email>/', views.user, name='user'),
    path('user-create/', views.userCreate, name='userCreate'),
    path('user-update/<str:pk>/', views.userUpdate, name='userUpdate'),
    path('products/', views.products, name='products'),
    path('product/<str:pk>/', views.product, name='product'),
    path('products/<str:email>/', views.specificProducts, name='specificProducts'),
    path('product-delete/<str:pk>/', views.productDelete, name='productDelete'),
    path('farmers/product-create/', views.productCreate, name='productCreate'),

    path('vendors/products/', views.vendorProducts, name='vendorProducts'),
    path('vendors/product/<str:pk>/', views.vendorProduct, name='vendorProduct'),
    path('vendors/products/<str:email>/', views.specificVendorProducts, name='specificVendorProducts'),
    path('vendors/product-create/', views.vendorProductCreate, name='vendorProductCreate'),
    path('vendors/product-update/<str:pk>/', views.vendorProductUpdate, name='vendorProductUpdate'),

    path('orders/', views.orders, name='orders'),
    path('order/<str:pk>/', views.order, name='order'),
    path('orders/create/', views.orderCreate, name='orderCreate'),
    path('orders/update/<str:pk>/', views.orderUpdate, name='orderUpdate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)