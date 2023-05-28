from django.contrib import admin
from django.contrib.auth.models import Group

from belka_emarket.participants.models import base_model
from belka_emarket.participants.models.participants_models import *


@admin.register(base_model.Address)
class Address(admin.ModelAdmin):
    list_display = ['country', 'city', 'street', 'house_number']


@admin.register(base_model.Product)
class Product(admin.ModelAdmin):
    list_display = ['title', 'model', 'release_date']
    ordering = ['-release_date', 'title']


@admin.action(description='Очистить задолженность')
def make_zero(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'debt', 'address']
    list_display_links = ('title',)
    filter_horizontal = ['product']
    actions = [make_zero]

    def address(self, obj):
        return obj.addres.city

    address.admin_order_field = 'address__city'


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'debt', 'address']
    list_display_links = ('title',)
    filter_horizontal = ['product']
    actions = [make_zero]

    def address(self, obj):
        return obj.addres.city

    address.admin_order_field = 'address__city'


@admin.register(IndividualEntrepreneur)
class SoleTraderAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'debt', 'address']
    list_display_links = ('title',)
    filter_horizontal = ['product']
    actions = [make_zero]

    def address(self, obj):
        return obj.addres.city

    address.admin_order_field = 'address__city'
