from rest_framework import serializers
from .models import Team, customerContats, dataInvoice

class ItemSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ItemSerializer2(serializers.ModelSerializer):
    class Meta:
        model = customerContats
        fields = '__all__'

class ItemSerializer3(serializers.ModelSerializer):
    class Meta:
        model = dataInvoice
        fields = '__all__'
