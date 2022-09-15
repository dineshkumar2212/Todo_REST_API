from django.shortcuts import render
from todoapp.models import userDetail,taskDetail
from rest_framework import viewsets
from todoapp.serializer import taskSerializer, userSerializer
# Create your views here.
class userViewset(viewsets.ModelViewSet):
    queryset=userDetail.objects.all()
    serializer_class=userSerializer
    
class taskViewset(viewsets.ModelViewSet):
    queryset=taskDetail.objects.all()
    serializer_class=taskSerializer
    
