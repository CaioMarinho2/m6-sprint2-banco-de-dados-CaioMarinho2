from django.urls import path
from .views import FileViewDetail

urlpatterns = [
    path('stores/<str:store_name>', FileViewDetail.as_view() ),

]
