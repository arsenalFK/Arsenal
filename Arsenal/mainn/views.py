from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from .forms import PlRequestForm
from .models import News, Player

        #НОВОСТИ-BUTTON#
class NewsView(TemplateView):
    template_name = 'mainn/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        news = News.objects.all().order_by('-news_date')
        context.update(
            {'news':news}
        )
        return context



        #СОСТАВ-BUTTON#

class TeamView(TemplateView):
    template_name = 'mainn/team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        team = Player.objects.all().filter(player_compose=1)
        context.update(
            {'team':team}
        )
        return context

class TeamView2(TemplateView):
    template_name = 'mainn/team2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        team = Player.objects.all().filter(player_compose=2)
        context.update(
            {'team':team}
        )
        return context

def compose(request):
    return render(request, 'mainn/compose.html', {'compose':compose})

def player_info(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'mainn/player.html', {'player':player})



        #КАБИНЕТ-BUTTON#

def cabinet(request):
    return render(request, 'mainn/cabinet.html', {cabinet:'cabinet'})




        #ЗАЯВКИ-BUTTON#

def add(request):
    return render(request, 'mainn/add.html', {add:'add'})

def add_to_team(requrest):
    form = PlRequestForm
    return render(requrest, 'mainn/add_to_team_form.html', {form:'form'})