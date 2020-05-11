from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class News(models.Model):
    class Meta:
        ordering = ['news_date']
    news_title = models.CharField(max_length=255, verbose_name='Заголовок')
    news_text = models.TextField(verbose_name='Текст')
    news_date = models.DateTimeField(auto_now_add=True)
    news_likes = models.IntegerField(default=0)
    news_image = models.ImageField(null=True, blank=True, verbose_name='Добавить изображение')

    def __str__(self):
        return self.news_title

class Player(models.Model):

    TYPE_GOALKEEPER = 1
    TYPE_DEFENDER = 2
    TYPE_MIDFIELDER = 3
    TYPE_FORWARD = 4
    TYPE_CHANGE = 5
    TYPE_MIDFIELDER2 = 6
    TYPE_CHOICES = (
        (TYPE_GOALKEEPER, 'Вратарь'),
        (TYPE_DEFENDER, 'Защитник'),
        (TYPE_MIDFIELDER, 'Полузащитник'),
        (TYPE_MIDFIELDER2, 'Полунападающий'),
        (TYPE_FORWARD, 'Нападающий'),
        (TYPE_CHANGE, 'На замене'),
    )

    player_image = models.ImageField(null=True, blank=True, help_text='Фото', verbose_name='Добавить фото')
    player_name = models.CharField(max_length=255, help_text='Имя игрока', verbose_name='Имя игрока')
    player_sur_name = models.CharField(max_length=255, help_text='Фамилия игрока', verbose_name='Фамилия игрока')
    player_age = models.SmallIntegerField(help_text='Возраст', verbose_name='Возраст')
    player_compose = models.ForeignKey('Compose', on_delete=models.CASCADE, default=1, help_text='Состав (I/II)', verbose_name='Состав')
    player_position = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=TYPE_CHANGE, help_text='Позиция', verbose_name='Игровая позиция')
    player_GK = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)], verbose_name='Вратарь',
                                         help_text='Показатель голкипера (мин - 1, макс - 99)')
    player_ATK = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)], verbose_name='Нападение',
                                          help_text='Показатель нападения (мин - 1, макс - 99)')
    player_MID = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)], verbose_name='Полузащита',
                                          help_text='Показатель полузащиты (мин - 1, макс - 99)')
    player_DEF = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)], verbose_name='Защита',
                                          help_text='Показатель защиты (мин - 1, макс - 99)')
    def __str__(self):
        return self.player_sur_name

class Compose(models.Model):

    TYPE_I = 1
    TYPE_II = 2
    TYPE_CHOICES = (
        (TYPE_I, 'Первый состав'),
        (TYPE_II, 'Второй состав'),
    )

    compose_name = models.CharField(max_length=255)
    compose = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=TYPE_I)

    def __str__(self):
        return self.compose_name

class PlayerRequest(models.Model):

    player_request_name = models.CharField(max_length=255, verbose_name='Имя')
    player_request_name2 = models.CharField(max_length=255, verbose_name='Фамилия')
    player_request_age = models.SmallIntegerField(default=0, verbose_name='Возраст')
    player_request_contacts = models.TextField(verbose_name='Контакты', help_text='Ном.Тел, Viber, WhatsApp, Skype')

    def __str__(self):
        return self.player_request_name2