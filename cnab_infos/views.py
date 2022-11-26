from .serializer import OperationsSerializer
from rest_framework.views import  Response, status,Request
from rest_framework import viewsets
from .models import File
from .serializer import FileSerializer

# Create your views here.

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
        
             


 

        

