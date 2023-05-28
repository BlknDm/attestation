from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from belka_emarket.participants.models.participants_models import *
from belka_emarket.participants.serializers.participants_serializers import *


class IndividualEntrepreneurCreateView(CreateAPIView):
    model = IndividualEntrepreneur
    serializer_class = IndividualEntrepreneurCreateSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated]


class IndividualEntrepreneurListView(ListAPIView):
    model = IndividualEntrepreneur
    serializer_class = IndividualEntrepreneurListSerializer
    queryset = IndividualEntrepreneur.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__country']
    permission_classes = [IsAuthenticated]


class IndividualEntrepreneurRetrieveView(RetrieveUpdateDestroyAPIView):
    model = IndividualEntrepreneur
    serializer_class = IndividualEntrepreneurUpdateSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated]
