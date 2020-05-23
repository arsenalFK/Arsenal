from django.urls import path
from . import views
from .views import NewsView, TeamView, TeamView2, AllRequestsView, AllTeamView

urlpatterns = [
    #НОВОСТИ + СОСТАВ#
    path('', NewsView.as_view(), name='news'),
    path('add_news/', views.add_n, name='add_n'),
        path('team/', views.compose, name='compose'),
            path('team/compose/', TeamView.as_view(), name='compose_1'),
                path('team/compose2/', TeamView2.as_view(), name='compose_2'),
                    path('team/compose/<int:pk>/', views.player_info, name='p_info'),

    #КАБИНЕТ#

    path('cabinet/', views.cabinet, name='cabinet'),
    path('cabinet/all_requests/', AllRequestsView.as_view(), name='all_requests'),
        path('cabinet/all_requests/<int:pk>/', views.person, name='person'),
    path('cabinet/all_players/', AllTeamView.as_view(), name='all_players'),
    path('cabinet/add_player/', views.add_pl, name='add_player'),

    #ЗАЯВКИ#

    path('add/', views.add, name='add'),
    path('add/add_to_team/', views.add_to_team, name='add_to_team'),
    path('add/add_to_team/good', views.team_good, name='team_good'),

    #РАСПИСАНИЕ#

    path('timetable/', views.timetable, name='timetable'),
]
