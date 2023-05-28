from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from belka_emarket.participants.models.participants_models import *
from belka_emarket.participants.serializers.participants_serializers import *


class FactoryCreateView(CreateAPIView):
    model = Factory
    serializer_class = FactoryCreateSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated]


class FactoryListView(ListAPIView):
    model = Factory
    serializer_class = FactoryListSerializer
    queryset = Factory.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__country']
    permission_classes = [IsAuthenticated]


class FactoryRetrieveView(RetrieveUpdateDestroyAPIView):
    model = Factory
    serializer_class = FactoryUpdateSerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated]
