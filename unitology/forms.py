# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings

from models import UnitsFieldMixin
from form_fields import BaseField, BaseMultiField

__all__ = ['UnitsFieldFormMixin']


class UnitsFieldFormMixin(forms.ModelForm):

    class Media:
        js = (
            settings.STATIC_URL + 'unitology/js/units_change.js',
            )

    def __init__(self, *args, **kwargs):
        super(UnitsFieldFormMixin, self).__init__(*args, **kwargs)
        try:
            units = self.instance.units
        except:
            units = UnitsFieldMixin.DEFAULT

        for field_name in self.fields.keys():
            if issubclass(self.fields[field_name].__class__, (BaseField, BaseMultiField)):
                self.fields[field_name].units = units
