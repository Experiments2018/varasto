from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatumgame'
    players_per_group = 2
    num_rounds = 1
    endowment = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    yesno=models.BooleanField(widget=widgets.RadioSelectHorizontal,
                                 )

    offer=models.CurrencyField(min=0,
                                    max=Constants.endowment,
                                    verbose_name='How much money you want to send?',
                                    doc="agent1 decision")
    def set_payoffs(self):
        agent1 = self.get_player_by_role('agent1')
        agent2 = self.get_player_by_role('agent2')
        agent1.payoff = Constants.endowment - self.offer
        agent2.payoff = self.offer




class Player(BasePlayer):

    gender = models.IntegerField(choices=
                                 ((0,'female'),
                                  (1,'male'),
                                  (2,"don't know")),
                                 widget=widgets.RadioSelectHorizontal,
                                 )



    def role(self):
        if self.id_in_group==1:
            return 'agent1'
        else:
            return 'agent2'
