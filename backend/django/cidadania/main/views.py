from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CandidateSerializer
from .models import Candidate
# Create your views here.

@api_view(['GET'])
def homepage_api(request, format=None):
    return Response('Bem vindo ao CidadaniaJá!!')

@api_view(['GET', 'POST'])
def candidates(request, format=None):

    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        data = request.data
        serializer = CandidateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)



@api_view(['GET', 'PUT', 'DELETE'])
def candidate(request, id,format=None):  
  
    try:
        candidate = Candidate.objects.get(pk=id)

    except Candidate.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = CandidateSerializer(candidate,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.erros, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        serializer = CandidateSerializer(candidate)
        print(serializer.data)
        candidate.delete()
        return Response(serializer.data, status.HTTP_200_OK)
    

