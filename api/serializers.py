from rest_framework import serializers

from .models import *

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'preco']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class ServicoRealizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoRealizado
        fields = ['id', 'nome_servico', 'descricao', 'preco', 'data']
        extra_kwargs = {
            'id': {'read_only': True}
        }

