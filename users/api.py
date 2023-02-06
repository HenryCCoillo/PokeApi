from .serializers import PagoSerializer
from .models import Pago
from rest_framework import viewsets,filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PagoViewSet(APIView):
    todos = Pago.objects.all()


    def get(self, request):
        todos = Pago.objects.all()
        serializer = PagoSerializer(todos, many=True)
        return Response(serializer.data)

    def delete(self, request):
        Pago.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        serializer = PagoSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer)
            print("sfds-----------------------------------")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import get_object_or_404
from .paginations import StandardResultsSetPagination

class PagoModelViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()

    serializer_class = PagoSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['user','servicio_pago','fecha_pago']
    
    throttle_scope = 'get'

    def get_serializer_class(self):
        return PagoSerializer

    def list(self,request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page,many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PagoSerializer(self.queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todo = get_object_or_404(self.queryset,pk=pk)
        serializer = PagoSerializer(todo)
        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data,list):
            serializer = PagoSerializer(data=request.data, many=True)
        else:
            serializer= PagoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        