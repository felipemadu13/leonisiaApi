from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import *

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'preco', 'data']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class ServicoRealizadoSerializer(serializers.ModelSerializer):
    servico = ServicoSerializer()  # Aceita um objeto de serviço completo

    class Meta:
        model = ServicoRealizado
        fields = ['id', 'servico']

    def create(self, validated_data):
        servico_data = validated_data.pop('servico')  # Extrai dados do serviço
        servico, _ = Servico.objects.get_or_create(**servico_data)  # Cria ou obtém o serviço
        return ServicoRealizado.objects.create(servico=servico, **validated_data)


class ServicoRealizadoGetSerializer(serializers.ModelSerializer):
    servico = ServicoSerializer()

    class Meta:
        model = ServicoRealizado
        fields = ['id', 'servico']

class TransacoesSerializer(serializers.ModelSerializer):
    servicosRealizados = ServicoRealizadoSerializer(many=True)  # Usa o serializer ajustado

    class Meta:
        model = Transacoes
        fields = ['id', 'tipo', 'data', 'metodoPagamento', 'valor', 'servicosRealizados']

    def create(self, validated_data):
        servicos_realizados_data = validated_data.pop('servicosRealizados', [])
        transacao = Transacoes.objects.create(**validated_data)

        # Cria os serviços realizados e associa à transação
        for servico_realizado_data in servicos_realizados_data:
            servico_realizado = ServicoRealizadoSerializer.create(
                ServicoRealizadoSerializer(),
                validated_data=servico_realizado_data
            )
            transacao.servicosRealizados.add(servico_realizado)

        return transacao
