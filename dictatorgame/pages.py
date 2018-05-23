from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Intro(Page):
    pass

class Decision(Page):
    form_model = 'group'
    form_fields = ['dg_decision']

    def is_displayed(self):
        return self.player.role() == 'dictator'

class ResultsWaitPage(WaitPage):
    #body_text = 'please wait dictator'
    def after_all_players_arrive(self):
        pass




class Results(Page):
    def vars_for_template(self):
        dicshare = 100-self.group.dg_decision
        return {'dictators_share': dicshare}


page_sequence = [
    Intro,
    Decision,
    ResultsWaitPage,
    Results
]
