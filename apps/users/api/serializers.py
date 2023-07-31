from rest_framework import serializers

from apps.users.models import House


class UserSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    email = serializers.CharField()

    def validate(self, attrs): #1 ciclo de vida
        nombre = attrs.get("nombre")
        email = attrs.get("email")
        if not "@" in email:
            raise serializers.ValidationError({"email": "No hay @"})
        
        if not "." in email.split("@")[1]: 
            raise serializers.ValidationError({"email": "No hay ."})

        return super().validate(attrs)
    
    def create(self, validated_data): #2 ciclo de vida
        return super().create(validated_data)
    
    def to_representation(self, instance): #3 ciclo de vida
        represetation =  super().to_representation(instance) # esto retorna un dict
        return represetation


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ["id","name"]

    def create(self, validated_data): # post
        # name = validated_data["name"]
        # name_body = validated_data.get("name")
        new_house = House.objects.create(**validated_data)
        return new_house

    def update(self, instance, validated_data): # put
        instance.name = validated_data.get("name")
        instance.save()
        return instance
    
    def to_representation(self, instance): # como se represta
        return super().to_representation(instance)


class HouseSerializer2(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ["id"]



class Serializer(serializers.Serializer):
    # campo 1
    # campo 2
    # etc
    # ...
    pass


class ModelSerializer(serializers.ModelSerializer):
    # tener class Meta
    pass

