# api\views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Servico
from .serializers import *

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Você está logado como {username}.")
                return redirect('home')  # Altere 'home' para a URL desejada após login
            else:
                messages.error(request, "Nome de usuário ou senha inválidos.")
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Agora você pode fazer login.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

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
        serializer = ServicoRealizadoGetSerializer(servicos_realizados, many=True)
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
        serializer = ServicoRealizadoGetSerializer(servico_realizado)
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
        serializer = TransacoesSerializer(data=nova_transacao)

        if serializer.is_valid():
            transacao = serializer.save()
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
