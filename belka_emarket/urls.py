from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth', include('rest_framework.urls')),
    path('factory/', include('belka_emarket.participants.urls.factory_urls')),
    path('retail_network/', include('belka_emarket.participants.urls.retail_network_urls')),
    path('individual_entrepreneur/', include('belka_emarket.participants.urls.individual_entrepreneur_urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls'))
    ]