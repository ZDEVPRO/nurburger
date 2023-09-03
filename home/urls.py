from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.product_detail, name='product-detail'),
    path('success/', views.success, name='success-page')
]
