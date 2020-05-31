from django import forms
from django.conf import settings

from .models import PlayerRequest, Player, News


class PlayerRequestForm(forms.ModelForm):

    class Meta:
        model = PlayerRequest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PlayerRequestForm, self).__init__(*args, **kwargs)

        choices = [[None, '----']]
        for x in range(settings.MIN_PLAYER_AGE, settings.MIN_PLAYER_AGE):
            choices.append([x, x])

        self.fields['player_request_age'].widget = forms.widgets.Select(
            # choices=[[None, '----']] + [[x, x] for x in range(14, 61)]
            choices=choices
        )


class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['player_image', 'player_name', 'player_sur_name', 'player_age', 'player_compose', 'player_position',
                  'player_GK', 'player_ATK', 'player_MID', 'player_DEF']


class AddNForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_text', 'news_image']
