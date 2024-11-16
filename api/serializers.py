from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import *

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'preco']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class ServicoRealizadoSerializer(serializers.ModelSerializer):
    servico = serializers.PrimaryKeyRelatedField(queryset=Servico.objects.all())

    class Meta:
        model = ServicoRealizado
        fields = ['id', 'data', 'servico']

class ServicoRealizadoGetSerializer(serializers.ModelSerializer):
    servico = ServicoSerializer()

    class Meta:
        model = ServicoRealizado
        fields = ['id', 'data', 'servico']

class TransacoesSerializer(serializers.ModelSerializer):
    servicosRealizados = ServicoRealizadoSerializer(many=True, required=False)

    class Meta:
        model = Transacoes
        fields = ['id', 'tipo', 'data', 'metodoPagamento', 'valor', 'servicosRealizados']

    def create(self, validated_data):

        servicos_realizados_data = validated_data.pop('servicosRealizados', [])

        transacao = Transacoes.objects.create(**validated_data)


        servicos_realizados = []
        for servico_data in servicos_realizados_data:

            servico_realizado = ServicoRealizado.objects.create(
                servico=Servico.objects.get(id=servico_data['servico']), 
                data=servico_data['data']
            )
            servicos_realizados.append(servico_realizado)
  
        transacao.servicosRealizados.add(*servicos_realizados)

        return transacao
