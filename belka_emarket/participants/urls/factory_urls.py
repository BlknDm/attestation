from django.urls import path

from belka_emarket.participants.views.factory_views import *

urlpatterns = [
    path('create/', FactoryCreateView.as_view(), name='factory_create'),
    path('list/', FactoryListView.as_view(), name='factory_list'),
    path('<int:pk>/', FactoryRetrieveView.as_view(), name='factory_RUD'),
]