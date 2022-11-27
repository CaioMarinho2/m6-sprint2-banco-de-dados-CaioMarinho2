from .serializer import OperationsSerializer
from rest_framework.views import  Response, status,Request, APIView
from rest_framework import viewsets
from .models import File, Operations
from .serializer import FileSerializer
from utils.utils import convert_transactions
from django.shortcuts import get_list_or_404
# Create your views here.

# Taking the operations that come from the CNAB document and registering them in the bank along with the document
class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
    def create(self, request:Request, *args, **kwargs):
        try:
            if len(request.FILES.keys())==0:
                return Response({"message":"you need to select a .txt file"},status.HTTP_400_BAD_REQUEST)
            
            # getting every Operation from every line of the document
            file_informations=request.FILES["File"].readlines() 
        
            #passing to string and formatting each operation
            operations_list = []
            for operations in file_informations:
                operations_list.append(operations.decode('utf-8').rstrip()) 
                
            # passing the operations to object format to be able to save in the database
            return_operations = []
            for save_operations in operations_list:
                normalized_value=int(save_operations[9:19])/100
                
                operation={
                    "type":save_operations[0:1],
                    "date":f"{save_operations[7:9]}/{save_operations[5:7]}/{save_operations[1:5]}",
                    "value":normalized_value,
                    "cpf":save_operations[19:30],
                    "card":save_operations[30:42],
                    "hour": f"{save_operations[42:44]}:{save_operations[44:46]}:{save_operations[46:48]}"  ,
                    "store_owner":save_operations[48:62].strip(),
                    "store_name":save_operations[62:80],
                    }
                
                # saving operations in the database
                serializer=OperationsSerializer(data=operation)
                serializer.is_valid(raise_exception=True)
                serializer.save()  
                return_operations.append(operation)
                
            # saving the document in the database    
            serializer= self.get_serializer(data=request.FILES)
            serializer.is_valid(raise_exception=True,)
            serializer.save() 
                
            return Response(return_operations,status.HTTP_201_CREATED)
        except ValueError :
            return Response({"message":"you need to select a valid CNAB.txt file, no blank lines and with each operation on one line"},status.HTTP_400_BAD_REQUEST)
        
        
class FileViewDetail(APIView):
    def get(self,request:Request,store_name:str) :
        #Searching operations via company name
        Operations_store= get_list_or_404(Operations,store_name=store_name)
        operations_to_return={
                "store_name":store_name,
                "operations": [],
                "balance":""
            }
        balance=0
        for operations_to_show in Operations_store:
            
            #getting the operation name by type
            type_operations=convert_transactions(operations_to_show.type, operations_to_show.value)
            
            #organizing the data that will be returned
            operations_corrects={
                "date":operations_to_show.date,
                "hour": operations_to_show.hour,
                "value": operations_to_show.value,
                "operation_name":type_operations["type"],
            }
            
            #calculating the company balance
            balance = round(balance+type_operations["value"],2)
            operations_to_return["balance"]=balance
            operations_to_return["operations"].append(operations_corrects)
         
        return Response(operations_to_return)
               