from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers import (
    HouseSerializer,
    HouseSerializer2
)
from apps.users.models import House



class HouseModelViewSet(viewsets.ModelViewSet):
    model = House
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    # def get_queryset(self):
    #     queryset = House.objects.all()
    #     return queryset

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return HouseSerializer2
    #     elif self.action in ['create', 'update']:
    #         return HouseSerializer
    
    # def list(self, request, *args, **kwargs):
    #     houses = self.get_queryset()
    #     serializer = self.get_serializer_class()
    #     data = serializer(houses, many=True)
    #     return Response(data.data)




# class UsersList(APIView): 
#     def get(self, request, *args, **kwargs): 
#         return Response(status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs): 
#         # request.POST # django monolitico aqui vienen los datos/body
#         # request.data # drf aqui vienen los datos/body
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class HouseAPIView(APIView): 
#     def get(self, request, *args, **kwargs): 
#         houses = House.objects.all()
#         serializer = HouseSerializer(instance=houses, many=True)   
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs): 
#         pass

#     def retrieve(self, request, *args, **kwargs):
#         house = House.objects.get(pk=kwargs['pk'])
#         serializer = HouseSerializer(instance=house)
#         return Response(serializer.data)
    