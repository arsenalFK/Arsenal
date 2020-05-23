from django import forms
from django.forms import ModelForm

from .models import PlayerRequest, Player, News


class PlayerRequestForm(forms.ModelForm):
    class Meta:
        model = PlayerRequest
        fields = ['player_request_name', 'player_request_name2', 'player_request_age', 'player_request_contacts',]

class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['player_image', 'player_name', 'player_sur_name', 'player_age', 'player_compose', 'player_position',
                  'player_GK', 'player_ATK', 'player_MID', 'player_DEF']

class AddNForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_text', 'news_image']