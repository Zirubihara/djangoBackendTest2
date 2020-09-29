from django.contrib.auth.mixins import LoginRequiredMixin
from .serializer import CustomerSerializer
from .models import Customer
from .permissions import IsHighPermission
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class CustomerList(LoginRequiredMixin, generics.ListCreateAPIView):
    raise_exception = True
    permission_classes = [IsHighPermission]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['isCustomersWhoMadePurchase']



class CustomerDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    raise_exception = True
    permission_classes = [IsHighPermission]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
