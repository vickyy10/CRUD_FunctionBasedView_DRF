from django.shortcuts import render
from .models import Person
from rest_framework.response import Response
from . serializer import PersonModelSerializer
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


# /////// FUNCTION BASED VIEWS (FBV) //////


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Personview(request):

    #---------  GET METHOD----------

    if request.method == 'GET':
        data = Person.objects.all()
        serializer=PersonModelSerializer(data,many=True)
        return Response(serializer.data)
    
    
    # ----------  POST METHOD-----------

    if request.method == 'POST':
        serializer=PersonModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('added')
        return Response('not added')
    

    # ---------- PUT METHOD -------------
        
    if request.method == 'PUT':
        pk=request.data['id']
        obj=Person.objects.get(id=pk)
        print(request.data['id'])
        serializer=PersonModelSerializer(obj,data=request.data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated ...','data':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # -------------- PATCH ------------------


    if request.method =='PATCH':
        pk=request.data['id']
        obj=Person.objects.get(id=pk)
        serializer=PersonModelSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data partial Updated ...','data':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # ---------DELETE----------

    if request.method == 'DELETE':
        pk=request.data['id']
        obj=Person.objects.get(id=pk)
        obj.delete()
        return Response({'msg':'Data Deleted !!!'})
        
    
