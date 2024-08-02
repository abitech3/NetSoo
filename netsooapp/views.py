from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .models import User



class Register(APIView):
    def post(self , request):
        data = request.data
        print(data)
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status' : False,
                 'message' : serializer.errors
            })
        serializer.save()
        return Response({
            'status': True
        })

    
       
       
















