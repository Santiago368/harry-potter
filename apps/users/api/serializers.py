from rest_framework import serializers

from apps.users.models import House


class UserSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    email = serializers.CharField()

    def validate(self, attrs):
        nombre = attrs.get("nombre")
        email = attrs.get("email")
        if not "@" in email:
            raise serializers.ValidationError({"email": "No hay @"})
        
        if not "." in email.split("@")[1]: 
            raise serializers.ValidationError({"email": "No hay ."})

        return super().validate(attrs)
    
    def to_representation(self, instance):
        represetation =  super().to_representation(instance) # esto retorna un dict
        return represetation


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ["name"]

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
