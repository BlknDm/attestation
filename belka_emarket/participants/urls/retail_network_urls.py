from django.urls import path

from belka_emarket.participants.views.retail_network_views import *


urlpatterns = [
    path('create/', RetailNetworkCreateView.as_view(), name='commerc_net_create'),
    path('list/', RetailNetworkListView.as_view(), name='commerc_net_list'),
    path('<int:pk>/', RetailNetworkRetrieveView.as_view(), name='commerc_net_RUD'),
]