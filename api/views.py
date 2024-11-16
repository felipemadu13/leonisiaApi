from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        servico_realizado.delete()
        return Response({"message": "Servico realizado excluído com sucesso."}, status=status.HTTP_204_NO_CONTENT)


# TRANSAÇÕES


@api_view(['GET', 'POST'])
def get_transacoes(request):
    if request.method == "GET":
        transacoes = Transacoes.objects.all()
        serializer = TransacoesSerializer(transacoes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        nova_transacao = request.data
        servicos_realizados_data = nova_transacao.pop('servicosRealizados', [])

        serializer = TransacoesSerializer(data=nova_transacao)
        
        if serializer.is_valid():
            transacao = serializer.save()

            for servico_data in servicos_realizados_data:
                try:
                    servico = Servico.objects.get(id=servico_data['servico']) 
                except ObjectDoesNotExist:
                    return Response(
                        {"error": f"Serviço com ID {servico_data['servico']} não encontrado."},
                        status=status.HTTP_404_NOT_FOUND
                    )
                
                servico_realizado = ServicoRealizado.objects.create(
                    servico=servico,
                    data=servico_data['data']
                )
                transacao.servicosRealizados.add(servico_realizado)

            transacao.save() 
            return Response(TransacoesSerializer(transacao).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
def get_transacoes_by_id(request, id):
    try:
        transacao = Transacoes.objects.get(pk=id)
    except Transacoes.DoesNotExist:
        return Response({"error": "Transação não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransacoesSerializer(transacao)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        dados_atualizados = request.data
        serializer = TransacoesSerializer(transacao, data=dados_atualizados)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transacao.delete()
        return Response({"message": "Transação excluída com sucesso."}, status=status.HTTP_204_NO_CONTENT)
