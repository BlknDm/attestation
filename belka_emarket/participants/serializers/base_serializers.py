from rest_framework import serializers

from belka_emarket.participants.models.base_model import Address, Product


class AddressPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('country', 'city', 'street', 'house_number')


class ProductPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'model', 'release_date')
