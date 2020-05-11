from django.urls import path
from . import views
from .views import NewsView, TeamView, TeamView2

urlpatterns = [
    #НОВОСТИ + СОСТАВ#
    path('', NewsView.as_view(), name='news'),
    path('team/', views.compose, name='compose'),
    path('team/compose/', TeamView.as_view(), name='compose_1'),
    path('team/compose2/', TeamView2.as_view(), name='compose_2'),
    path('team/compose/<int:pk>/', views.player_info, name='p_info'),

    #КАБИНЕТ#

    path('cabinet/', views.cabinet, name='cabinet'),


    #ЗАЯВКИ#

    path('add/', views.add, name='add'),
    path('add/add_to_team/', views.add_to_team, name='add_to_team'),
]
