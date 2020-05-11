from django.contrib import admin

# Register your models here.
from .models import News, Player, Compose, PlayerRequest

admin.site.register(News)
admin.site.register(Player)
admin.site.register(Compose)
admin.site.register(PlayerRequest)