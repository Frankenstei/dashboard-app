from django.shortcuts import render
from rest_framework import generics
from .models import Team, customerContats, dataInvoice
from .serializers import ItemSerializer1, ItemSerializer2, ItemSerializer3
from rest_framework.response import Response

# Create your views here.
class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = ItemSerializer1

class TeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = ItemSerializer1

class CustomerContactsListCreateView(generics.ListCreateAPIView):
    queryset = customerContats.objects.all()
    serializer_class = ItemSerializer2

class CustomerContactsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = customerContats.objects.all()
    serializer_class = ItemSerializer2

class dataInvoiceListCreateView(generics.ListCreateAPIView):
    queryset = dataInvoice.objects.all()
    serializer_class = ItemSerializer3

class dataInvoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = dataInvoice.objects.all()
    serializer_class = ItemSerializer3

class UserCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = ItemSerializer1

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
