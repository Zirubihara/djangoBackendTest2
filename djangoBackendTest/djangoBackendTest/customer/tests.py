from http import client

from django.contrib.auth.models import User
from requests.auth import HTTPBasicAuth
from rest_framework.test import APIClient

from djangobackendtest.djangoBackendTest.djangoBackendTest.users.models import CustomUser

user = CustomUser.objects.get(email='kanek@anulujkredyt.pl')
client = APIClient()