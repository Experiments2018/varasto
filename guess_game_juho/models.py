from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'guess_game_juho'
    players_per_group = None
    num_rounds = 1

    endowment = 100

    minarvaus = 0
    maxarvaus = 100

    juho_constant = 555


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    toguess = models.IntegerField(min=Constants.minarvaus,
                                  max=Constants.maxarvaus,)
    guess = models.IntegerField()



