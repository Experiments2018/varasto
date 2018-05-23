from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    def before_next_page(self):
        toguess = random.randint(Constants.minarvaus, Constants.maxarvaus)
        self.player.toguess = toguess

class Decision(Page):
    form_model = 'player'
    form_fields = ['guess']

    def before_next_page(self):
        self.player.payoff = Constants.endowment - abs(self.player.toguess-self.player.guess)

        self.player.difference = abs(self.player.toguess - self.player.guess)

class Results(Page):
    def vars_for_template(self):
        dif = abs(self.player.toguess-self.player.guess)
        return {'dif':dif}


page_sequence = [
    Intro,
    Decision,
    Results
]
