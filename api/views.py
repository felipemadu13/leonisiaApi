from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Servico
from .serializers import *

@api_view(['GET', 'POST'])
def get_servicos(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        novo_servico = request.data
        serializer = ServicoSerializer(data=novo_servico)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_servicos_by_id(request, id):
    try:
        servico = Servico.objects.get(pk=id)
    except Servico.DoesNotExist:
        return Response({"error": "Servico não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServicoSerializer(servico)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        dados_atualizados = request.data
        serializer = ServicoSerializer(servico, data=dados_atualizados)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        servico.delete()
        return Response({"message": "Servico excluído com sucesso."}, status=status.HTTP_204_NO_CONTENT)
