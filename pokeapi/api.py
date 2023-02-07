
from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated  

from .paginations import StandardResultsSetPagination
# from ..users.paginations import StandardResultsSetPagination

class PokemonModelViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    pagination_class = StandardResultsSetPagination
    
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return PokemonSerializer

    def list(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page,many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = PokemonSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            if int(pk):
                pokemon = Pokemon.objects.filter(id=pk).first()
                serializer = PokemonSerializer(pokemon)
                return Response(serializer.data)
        except:
            pokemon = Pokemon.objects.filter(name=pk).first()
            serializer = PokemonSerializer(pokemon)
            return Response(serializer.data)



class PokemonViewSet(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        todos = Pokemon.objects.all()
        serializer = PokemonSerializer(todos, many=True)
        return Response(serializer.data)




class PokemonOneViewSet(APIView):
    def get(self, request,id):
        try:
            if int(id):
                pokemon = Pokemon.objects.filter(id=id).first()
                serializer = PokemonSerializer(pokemon)
                return Response(serializer.data)
        except:
            pokemon = Pokemon.objects.filter(name=id).first()
            serializer = PokemonSerializer(pokemon)
            return Response(serializer.data)


