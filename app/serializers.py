from rest_framework import serializers

from .models import Car, Hotel, Travel


class TravelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    price = serializers.FloatField()
    tariff = serializers.IntegerField()
    car_id = serializers.IntegerField()
    hotel_id = serializers.IntegerField()

    def create(self, validated_data):
        return Travel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.comment)
        instance.duration = validated_data.get('duration', instance.lifetime)
        instance.price = validated_data.get('price', instance.price)
        instance.car_id = validated_data.get('car_id', instance.klass_id)
        instance.hotel_id = validated_data.get('hotel_id', instance.hotel_id)
        instance.save()
        return instance


class HotelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    stars = serializers.IntegerField(default=0)
    price = serializers.FloatField()

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    price = serializers.FloatField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

