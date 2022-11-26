from rest_framework import serializers
from .models import Operations,File

class OperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Operations
        fields=["id","type","date","value","cpf","card","hour","store_owner","store_name"]
        read_only_fields = ["id"]
        
class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'
       