from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView, ListView, CreateView

from .forms import PlayerRequestForm, AddPlayerForm, AddNForm
from .models import News, Player, PlayerRequest


#НОВОСТИ-BUTTON#
class NewsView(TemplateView):
    template_name = 'mainn/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        news = News.objects.all().order_by('-news_date')
        context['news'] = news
        return context


def add_n(request):
    if request.method == 'POST':
        form = AddNForm(request.POST, request.FILES)
        if form.is_valid():
            add_news = form.save()
            add_news.save()
            return redirect('news')
    else:
        form = AddNForm
        return render(request, 'mainn/add_n.html', {
            'form': form
        })




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


class AllTeamView(TemplateView):
    template_name = 'mainn/all_team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        all = Player.objects.all()
        context.update({
            'all':all
        })
        return context


def compose(request):
    return render(request, 'mainn/compose.html', {'compose':compose})


def player_info(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'mainn/player.html', {'player':player})



        #КАБИНЕТ-BUTTON#

class AllRequestsView(TemplateView):
    template_name = 'mainn/all_requests.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        requests = PlayerRequest.objects.all()
        context.update({
            'requests':requests
        })
        return context


def person(request, pk):
    per = get_object_or_404(PlayerRequest, pk=pk)
    return render(request, 'mainn/person.html', {'per':per})

def cabinet(request):
    return render(request, 'mainn/cabinet.html', {cabinet:'cabinet'})


class AddPlayer(CreateView):
    template_name = 'mainn/add_player.html'
    model = Player
    fields = '__all__'

# def add_pl(request):
#     if request.method == 'POST':
#         form = AddPlayerForm(request.POST)
#         if form.is_valid():
#             add_player = form.save()
#             add_player.save()
#             return redirect('all_players')
#     else:
#         form = AddPlayerForm
#         return render(request, 'mainn/add_player.html', {
#             'form': form
#         })

def contacts(request):
    return render(request, 'mainn/contacts.html',{
        contacts:'contacts'
    })


        #ЗАЯВКИ-BUTTON#

def add(request):
    return render(request, 'mainn/add.html', {add:'add'})

def add_to_team(requrest):
    if requrest.method == 'POST':
        form = PlayerRequestForm(requrest.POST)
        if form.is_valid():
            playerrequest = form.save()
            playerrequest.save()
            return redirect('team_good')
    else:
        form = PlayerRequestForm
    return render(requrest, 'mainn/add_to_team_form.html', {'form': form})

def team_good(request):
    return render(request, 'mainn/player_request_good.html', {
        team_good: 'team_good'
    })


            #РАСПИСАНИЕ#

def timetable(request):
    return render(request, "mainn/timetable.html", {
        timetable: 'timetable'
    })



