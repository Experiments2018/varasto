from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""
import random

class Constants(BaseConstants):
    name_in_url = 'politicalgame'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):



    def creating_session(self):
        for p in self.get_players():
            p.radical = random.choice([True, False])



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    radical = models.BooleanField()
    yrside = models.StringField(
        widget=widgets.RadioSelectHorizontal,
    )

    yrscale = models.IntegerField(choices=[
        (0,"0=Far left"),
        (1,1),
        (2, 2),
        (3, 3),
        (4,4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10,"10=Far rigth")
    ],
                                  widget=widgets.RadioSelectHorizontal, )
