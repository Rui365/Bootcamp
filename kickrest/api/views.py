from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Cham
from api.serializers import KickSerializer
# Create your views here.

class KickViewSet(viewsets.ModelViewSet):
    queryset = Cham.objects.all()
    serializer_class = KickSerializer
