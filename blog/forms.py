#  Copyright Joubi Kris (c) 2023.
#
from django import forms

from .models import Person, Room


class MoveForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('location',)

