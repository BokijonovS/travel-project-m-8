from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import TravelSerializer, CarSerializer, HotelSerializer
from .models import Hotel, Car, Travel

# Create your views here.


class TravelAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response({"travel": TravelSerializer(travel).data})
            except:
                return Response({"error": "Travel information not found!!"})

        travels = Travel.objects.all()
        return Response({"travels": TravelSerializer(travels, many=True).data})

    def post(self, request: Request):
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid()
        travel = serializer.save()
        return Response({"travel": TravelSerializer(travel).data, "message": "Travel added successfully!"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                serializer = TravelSerializer(travel, data=request.data)
                serializer.is_valid(raise_exception=True)
                updated_travel = serializer.save()
                return Response({"travel": TravelSerializer(updated_travel).data, "message": "Travel updated successfully!"})
            except:
                return Response({'error': "Travel not found"})

        return Response({"detail": "Method \"PUT\" not allowed."})

    def delete(self, request: Request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                travel.delete()
                return Response({'success': "Travel deleted successfully!"})
            except:
                return Response({'error': "Travel not found"})

        return Response({"detail": "Method \"DELETE\" not allowed."})


class CarAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                car = Car.objects.get(pk=pk)
                return Response({"Car": CarSerializer(car).data})
            except:
                return Response({"error": "Car Not found!"})

        cars = Car.objects.all()
        return Response({"car": CarSerializer(cars, many=True).data})

    def post(self, request: Request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid()
        car = serializer.save()
        return Response({"car": CarSerializer(car).data, "message": "Car added successfully!"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                car = Car.objects.get(pk=pk)
                serializer = CarSerializer(car, data=request.data)
                serializer.is_valid(raise_exception=True)
                updated_car = serializer.save()
                return Response({"car": CarSerializer(updated_car).data, "message": "Car updated successfully!"})
            except:
                return Response({'error': "Car not found!"})

        return Response({"detail": "Method \"PUT\" not allowed."})

    def delete(self, request: Request, pk=None):
        if pk:
            try:
                car = Car.objects.get(pk=pk)
                car.delete()
                return Response({'success': "Car deleted successfully!"})
            except:
                return Response({'error': "Car not found!"})

        return Response({"detail": "Method \"DELETE\" not allowed."})


class HotelAPIView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                hotel = Hotel.objects.get(pk=pk)
                return Response({"hotels": HotelSerializer(hotel).data})
            except:
                return Response({"error": "Hotel Not found!"})

        hotels = Hotel.objects.all()
        return Response({"hotel": HotelSerializer(hotels, many=True).data})

    def post(self, request: Request):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid()
        hotel = serializer.save()
        return Response({"hotel": HotelSerializer(hotel).data, "message": "Hotel added successfully!"})

    def put(self, request: Request, pk=None):
        if pk:
            try:
                hotel = Hotel.objects.get(pk=pk)
                serializer = HotelSerializer(hotel, data=request.data)
                serializer.is_valid(raise_exception=True)
                updated_hotel = serializer.save()
                return Response({"hotel": HotelSerializer(updated_hotel).data, "message": "Hotel updated successfully!"})
            except:
                return Response({'error': "Hotel not found!"})

        return Response({"detail": "Method \"PUT\" not allowed."})

    def delete(self, request: Request, pk=None):
        if pk:
            try:
                hotel = Hotel.objects.get(pk=pk)
                hotel.delete()
                return Response({'success': "Hotel deleted successfully!"})
            except:
                return Response({'error': "Hotel not found!"})

        return Response({"detail": "Method \"DELETE\" not allowed."})

