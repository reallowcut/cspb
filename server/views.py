from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone
from rest_framework import status

from .models import Illumination
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import IlluminationSerializer


def index(request):
    illuminations = Illumination.objects.all()
    context = {'illuminations': illuminations}
    return render(request, 'index.html', context)


class GetIlluminationInfoView(APIView):
    def get(self, request):
        # Получаем набор всех записей из таблицы Capital
        queryset = Illumination.objects.all()
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = IlluminationSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class GetLastInfoView(APIView):
    def get(self, request):
        queryset = Illumination.objects.latest('id')
        serializer_for_queryset = IlluminationSerializer(
            instance=queryset,
            many=False
        )
        return Response(serializer_for_queryset.data)


class GetAllTimeInfoView(APIView):
    def get(self, request):
        queryset = Illumination.objects.all()
        serializer_for_queryset = IlluminationSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


class GetInfoForWeekView(APIView):
    def get(self, request):
        start_date = timezone.now() - timedelta(days=7)
        queryset = Illumination.objects.filter(created_at__gte=start_date)

        serializer_for_queryset = IlluminationSerializer(
            instance=queryset,
            many=True 
        )
        return Response(serializer_for_queryset.data)


class PostInfoView(APIView):
    def post(self, request):
        print(request.data)
        new_data = request.data
        new_data['level'] = request.data['level']

        if request.data['level'] >= 580:
            new_data['illumination_class'] = 1
        elif 580 > request.data['level'] >= 400:
            new_data['illumination_class'] = 2
        elif 400 > request.data['level'] >= 150:
            new_data['illumination_class'] = 3
        elif request.data['level'] < 150:
            new_data['illumination_class'] = 4

        serializer = IlluminationSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
