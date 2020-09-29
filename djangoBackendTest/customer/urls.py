from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomerList, CustomerDetail

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)