from django.db import transaction
from rest_framework import serializers

from belka_emarket.participants.models.base_model import Address, Product
from belka_emarket.participants.models.participants_models import *
from belka_emarket.participants.serializers.base_serializers import AddressPartSerializer, ProductPartSerializer


class FactoryCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
    debt = serializers.DecimalField(max_digits=19, decimal_places=2, required=False)
    address = AddressPartSerializer(read_only=True)
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Factory
        fields = "__all__"
        read_only_fields = ("id", "created")

    def is_valid(self, *, raise_exception=False):
        self._address = self.initial_data.pop('address')
        self._product = self.initial_data.pop('product')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        with transaction.atomic():
            factory = Factory.objects.create(**validated_data)
            address, _ = Address.objects.get_or_create(**self._address)
            product, _ = Product.objects.get_or_create(**self._product)
            factory.address = address
            factory.product.add(product)
            factory.save()

        return factory


class FactoryListSerializer(serializers.ModelSerializer):
    address = AddressPartSerializer(
        read_only=True
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ('__all__',)


class FactoryUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    address = AddressPartSerializer(
        read_only=True,
        required=False
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ('id', 'created', 'debt')

    def is_valid(self, *, raise_exception=False):
        if 'address' in self.initial_data:
            self._address = self.initial_data.pop('address')
        else:
            self._address = None
        if 'product' in self.initial_data:
            self._product = self.initial_data.pop('product')
        else:
            self._product = None
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        factory = super().save()

        with transaction.atomic():
            if self._address:
                if factory.address is None:
                    address, _ = Address.objects.get_or_create(**self._address)
                else:
                    address, _ = Address.objects.update_or_create(id=factory.address.pk, defaults=self._address)
                factory.address = address
            if self._product:
                if factory.address is None:
                    product, _ = Product.objects.get_or_create(**self._address)
                else:
                    product, _ = Product.objects.update_or_create(self._product.pk, **self._product)
                factory.product.add(product)

            factory.save()

        return factory


class IndividualEntrepreneurCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
    debt = serializers.DecimalField(max_digits=19, decimal_places=2, required=False)
    address = AddressPartSerializer(read_only=True)
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = IndividualEntrepreneur
        fields = "__all__"
        read_only_fields = ("id", "created")

    def is_valid(self, *, raise_exception=False):
        self._address = self.initial_data.pop('address')
        self._product = self.initial_data.pop('product')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        with transaction.atomic():
            individual_entrepreneur = IndividualEntrepreneur.objects.create(**validated_data)
            address, _ = Address.objects.get_or_create(**self._address)
            product, _ = Product.objects.get_or_create(**self._product)
            individual_entrepreneur.address = address
            individual_entrepreneur.product.add(product)
            individual_entrepreneur.save()

        return individual_entrepreneur


class IndividualEntrepreneurListSerializer(serializers.ModelSerializer):
    address = AddressPartSerializer(
        read_only=True
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'
        read_only_fields = ('__all__',)


class IndividualEntrepreneurUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    address = AddressPartSerializer(
        read_only=True,
        required=False
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'
        read_only_fields = ('id', 'created', 'debt')

    def is_valid(self, *, raise_exception=False):
        if 'address' in self.initial_data:
            self._address = self.initial_data.pop('address')
        else:
            self._address = None
        if 'product' in self.initial_data:
            self._product = self.initial_data.pop('product')
        else:
            self._product = None
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        individual_entrepreneur = super().save()

        with transaction.atomic():
            if self._address:
                if individual_entrepreneur.address is None:
                    address, _ = Address.objects.get_or_create(**self._address)
                else:
                    address, _ = Address.objects.update_or_create(id=individual_entrepreneur.address.pk, defaults=self._address)
                individual_entrepreneur.address = address
            if self._product:
                if individual_entrepreneur.address is None:
                    product, _ = Product.objects.get_or_create(**self._address)
                else:
                    product, _ = Product.objects.update_or_create(self._product.pk, **self._product)
                individual_entrepreneur.product.add(product)

            individual_entrepreneur.save()

        return individual_entrepreneur


class RetailNetworkCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
    debt = serializers.DecimalField(max_digits=19, decimal_places=2, required=False)
    address = AddressPartSerializer(read_only=True)
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = RetailNetwork
        fields = "__all__"
        read_only_fields = ("id", "created")

    def is_valid(self, *, raise_exception=False):
        self._address = self.initial_data.pop('address')
        self._product = self.initial_data.pop('product')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        with transaction.atomic():
            retail_network = RetailNetwork.objects.create(**validated_data)
            address, _ = Address.objects.get_or_create(**self._address)
            product, _ = Product.objects.get_or_create(**self._product)
            retail_network.address = address
            retail_network.product.add(product)
            retail_network.save()

        return retail_network


class RetailNetworkListSerializer(serializers.ModelSerializer):
    address = AddressPartSerializer(
        read_only=True
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ('__all__',)


class RetailNetworkUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    address = AddressPartSerializer(
        read_only=True,
        required=False
    )
    product = ProductPartSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ('id', 'created', 'debt')

    def is_valid(self, *, raise_exception=False):
        if 'address' in self.initial_data:
            self._address = self.initial_data.pop('address')
        else:
            self._address = None
        if 'product' in self.initial_data:
            self._product = self.initial_data.pop('product')
        else:
            self._product = None
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        retail_network = super().save()

        with transaction.atomic():
            if self._address:
                if retail_network.address is None:
                    address, _ = Address.objects.get_or_create(**self._address)
                else:
                    address, _ = Address.objects.update_or_create(id=retail_network.address.pk, defaults=self._address)
                retail_network.address = address
            if self._product:
                if retail_network.address is None:
                    product, _ = Product.objects.get_or_create(**self._address)
                else:
                    product, _ = Product.objects.update_or_create(self._product.pk, **self._product)
                retail_network.product.add(product)

            retail_network.save()

        return retail_network