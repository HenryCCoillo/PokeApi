from rest_framework import serializers
from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
        read_only_fields = ['name','number','hp','attack','defense','special_attack','special_defense','speed','img']