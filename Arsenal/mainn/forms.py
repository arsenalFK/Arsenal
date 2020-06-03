from django import forms
from django.conf import settings

from .models import PlayerRequest, Player, News


class PlayerRequestForm(forms.ModelForm):
    class Meta:

        model = PlayerRequest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PlayerRequestForm, self).__init__(*args, **kwargs)

        self.fields['player_request_age'].widget = forms.widgets.Select(
        choices=[[None, '----']] + [[x, x] for x in range(14, 61)]
        )

class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddPlayerForm, self).__init__(*args, **kwargs)

        self.fields['height'].widget = forms.widgets.Select(
            choices=[[None, '---']] + [[i, i] for i in range(140, 221)]
        )
        self.fields['weight'].widget = forms.widgets.Select(
            choices=[[None, '---']] + [[i, i] for i in range(0, 160)]
        )

class AddNForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_text', 'news_image']