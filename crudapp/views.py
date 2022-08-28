from django.shortcuts import render
from .serializers import UserSerializers
from .models import user
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class crudapi(APIView):
    
    def post(self, request, format=None):
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        usr = user.objects.all()
        serializer = UserSerializers(usr, many=True)
        return Response(serializer.data)
    
class crud_pk(APIView):
    
    def object_pk(self, pk):
        try:
            return user.objects.get(id=pk)
        except user.DoesNotExist:
            raise Exception('User does not exist')
        
    def get(self, request, pk, format=None):
        usr = self.object_pk(pk)
        serializer = UserSerializers(usr)
        return Response(serializer.data)
    
    
    def put(self, request, pk, format=None):
        usr = self.object_pk(pk)
        serializer = UserSerializers(usr, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        usr = self.object_pk(pk)
        usr.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)