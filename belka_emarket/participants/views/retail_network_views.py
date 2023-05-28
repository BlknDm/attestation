from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from belka_emarket.participants.models.participants_models import *
from belka_emarket.participants.serializers.participants_serializers import *


class RetailNetworkCreateView(CreateAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkCreateSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated]


class RetailNetworkListView(ListAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkListSerializer
    queryset = RetailNetwork.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__country']
    permission_classes = [IsAuthenticated]


class RetailNetworkRetrieveView(RetrieveUpdateDestroyAPIView):
    model = RetailNetwork
    serializer_class = RetailNetworkUpdateSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated]
