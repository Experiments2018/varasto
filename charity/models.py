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
    name_in_url = 'charity'
    players_per_group = None
    num_rounds = 1
    r_min = 1
    r_max = 100


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.personal_A = random.choice([True, False])
            p.personal_B = random.choice([True, False])
            p.endowment = random.randint(Constants.r_min, Constants.r_max)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    endowment = models.IntegerField()
    personal_A = models.BooleanField()
    personal_B = models.BooleanField()
    charity_donation = models.StringField(widget=widgets.RadioSelectHorizontal,
                                          choices=["Greenpeace", "RedCross"])
    don1  = models.IntegerField(verbose_name="Greenpeace")

    don2 = models.IntegerField(verbose_name="RedCross")

    # widget=widgets.RadioSelectHorizontal,
    #                                     choices=["Greenpeace", "RedCross"])
