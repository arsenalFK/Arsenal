from django import forms

from .models import PlayerRequest


class PlRequestForm(forms.ModelForm):
    class Meta:
        model = PlayerRequest
        fields = ['player_request_name', 'player_request_name2', 'player_request_age', 'player_request_contacts']