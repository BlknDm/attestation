from belka_emarket.participants.models.base_model import BaseModel
from django.db import models


class Factory(BaseModel):

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class IndividualEntrepreneur(BaseModel):
    title = models.ForeignKey('Factory', on_delete=models.SET_NULL, verbose_name='Производитель', null=True)

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'


class RetailNetwork(BaseModel):
    title = models.ForeignKey('Factory', on_delete=models.SET_NULL, verbose_name='Производитель', null=True)

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'
