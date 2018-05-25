from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Juho Ylimäki'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'publicgood'
    players_per_group = 3
    num_rounds = 3
    endowment = 100
    efficiency_factor = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.IntegerField()
    individual_share = models.IntegerField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share


class Player(BasePlayer):
    contribution = models.CurrencyField(min=0,
                                        max=Constants.endowment,
                                        verbose_name='How much money you want to contribute?',
                                        doc="playerdecision")

    check = models.BooleanField()