from rest_framework import serializers
from .models import Equipe, Jogador

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'

class EquipeSerializer(serializers.ModelSerializer):
    # Serialização aninhada: Lista os jogadores automaticamente
    jogadores = JogadorSerializer(many=True, read_only=True)

    class Meta:
        model = Equipe
        fields = ['id', 'nome', 'regiao', 'data_fundacao', 'jogadores']