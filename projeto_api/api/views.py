from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .pagination import *


class RegionList(APIView):
    def get(self, request):
        try:
            lista_Region = Region.objects.all()
            paginator = PaginacaoRegion()
            result_page = paginator.paginate_queryset(lista_Region, request)
            serializer = RegionSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = RegionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegionDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            region = Region.objects.get(pk=pk)
            serializer = RegionSerializer(region)
            return Response(serializer.data)
        except Region.DoesNotExist:
            return JsonResponse({'mensagem': "A Região não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            region = Region.objects.get(pk=pk)
            serializer = RegionSerializer(region, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Region.DoesNotExist:
            return JsonResponse({'mensagem': "A Região não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            region = Region.objects.get(pk=pk)
            region.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Region.DoesNotExist:
            return JsonResponse({'mensagem': "A Região não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FluitList(APIView):
    def get(self, request):
        try:
            lista_Fluit = Fluit.objects.all()
            paginator = PaginacaoRegion()
            result_page = paginator.paginate_queryset(lista_Fluit, request)
            serializer = FluitSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = FluitSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FluitDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            fluit = Fluit.objects.get(pk=pk)
            serializer = FluitSerializer(region)
            return Response(serializer.data)
        except Fluit.DoesNotExist:
            return JsonResponse({'mensagem': "A Fluit não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            fluit = Fluit.objects.get(pk=pk)
            serializer = FluitSerializer(fluit, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Fluit.DoesNotExist:
            return JsonResponse({'mensagem': "A Fruit não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            fluit = Fluit.objects.get(pk=pk)
            fluit.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Fluit.DoesNotExist:
            return JsonResponse({'mensagem': "A Fruit não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)