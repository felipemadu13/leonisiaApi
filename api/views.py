# api/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Servico, ServicoRealizado, Transacoes
from .serializers import ServicoSerializer, ServicoRealizadoSerializer, ServicoRealizadoGetSerializer, TransacoesSerializer

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.authtoken.models import Token


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)  # Gera um token se necessário
                print(f"Usuário autenticado com sucesso: {user}")  # Log de depuração
                return JsonResponse({'message': 'Login realizado com sucesso.', 'token': token.key})
            else:
                print("Falha na autenticação: Nome de usuário ou senha incorretos.")  # Log de depuração
                return JsonResponse({'error': 'Nome de usuário ou senha incorretos.'}, status=400)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Dados inválidos. Certifique-se de enviar "username" e "password".'}, status=400)
    return JsonResponse({'error': 'Método não permitido.'}, status=405)

@csrf_exempt
def user_logout(request):
    
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout realizado com sucesso.'})

    return JsonResponse({'error': 'Método não permitido.'}, status=405)


@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Usuário já existe.'}, status=400)
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'message': 'Usuário registrado com sucesso.'}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Dados inválidos. Certifique-se de enviar "username" e "password".'}, status=400)

    return JsonResponse({'error': 'Método não permitido.'}, status=405)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_servicos(request):
    print(f"Requisição recebida com método {request.method} do usuário {request.user}")    
    if request.method == 'GET':
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServicoSerializer(data=request.data)
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
