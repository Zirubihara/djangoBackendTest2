from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .serializer import CustomerSerializer
from .models import Customer
from .permissions import HighPermissions
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
# @login_required
class CustomerList(LoginRequiredMixin, generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    raise_exception = True
    permission_classes = [HighPermissions]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['has_purchase_history']


# @login_required
class CustomerDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    raise_exception = True
    permission_classes = [HighPermissions]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
