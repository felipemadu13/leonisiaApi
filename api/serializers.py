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
    servico = serializers.PrimaryKeyRelatedField(queryset=Servico.objects.all())

    class Meta:
        model = ServicoRealizado
        fields = ['id', 'servico', 'data']
        extra_kwargs = {
            'id': {'read_only': True}
        }

