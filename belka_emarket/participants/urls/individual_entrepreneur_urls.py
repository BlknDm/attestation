from django.urls import path

from belka_emarket.participants.views.individual_entrepreneur_views import *

urlpatterns = [
    path('create/', IndividualEntrepreneurCreateView.as_view(), name='individual_entrepreneur_create'),
    path('list/', IndividualEntrepreneurListView.as_view(), name='individual_entrepreneur_list'),
    path('<int:pk>/', IndividualEntrepreneurRetrieveView.as_view(), name='individual_entrepreneur_RUD'),
]