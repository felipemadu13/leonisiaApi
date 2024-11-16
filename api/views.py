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
    
# View para listar e criar ServicosRealizados
@api_view(['GET', 'POST'])
def get_servicos_realizados(request):
    if request.method == "GET":
        servicos_realizados = ServicoRealizado.objects.all()
        serializer = ServicoRealizadoSerializer(servicos_realizados, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        novo_servico_realizado = request.data
        serializer = ServicoRealizadoSerializer(data=novo_servico_realizado)

        if serializer.is_valid():
            # Não é necessário enviar 'descricao' ou 'preco' no POST, pois já estão no Servico
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View para obter, atualizar ou excluir um ServicoRealizado específico
@api_view(['GET', 'PUT', 'DELETE'])
def get_servicos_realizados_by_id(request, id):
    try:
        servico_realizado = ServicoRealizado.objects.get(pk=id)
    except ServicoRealizado.DoesNotExist:
        return Response({"error": "Servico realizado não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServicoRealizadoSerializer(servico_realizado)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        dados_atualizados = request.data
        serializer = ServicoRealizadoSerializer(servico_realizado, data=dados_atualizados)

        if serializer.is_valid():
            # Não é necessário enviar 'descricao' ou 'preco' no PUT, pois já estão no Servico
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        servico_realizado.delete()
        return Response({"message": "Servico realizado excluído com sucesso."}, status=status.HTTP_204_NO_CONTENT)
