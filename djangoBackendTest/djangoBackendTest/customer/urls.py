from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomerList, CustomerDetail

urlpatterns = [
    path('customer/', CustomerList.as_view(), name='list'),
    path('customer/<int:pk>/', CustomerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)