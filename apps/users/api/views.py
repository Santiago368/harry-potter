from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers import UserSerializer, HouseSerializer
from apps.users.models import House


class UsersList(APIView): 
    def get(self, request, *args, **kwargs): 
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs): 
        # request.POST # django monolitico aqui vienen los datos/body
        # request.data # drf aqui vienen los datos/body
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseAPIView(APIView): 
    def get(self, request, *args, **kwargs): 
        houses = House.objects.all()
        serializer = HouseSerializer(instance=houses, many=True)   
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs): 
        pass