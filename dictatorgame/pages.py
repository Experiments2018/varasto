from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Intro(Page):
    form_model = 'player'
    form_fields = ['gender']

class Decision(Page):
    form_model = 'group'
    form_fields = ['dg_decision']

    def is_displayed(self):
        return self.player.role() == 'dictator'

    def vars_for_template(self):
        receiver = self.group.get_player_by_role('receiver')
        sender = self.group.get_player_by_role('dictator')
        return {
                "receiver":receiver,
                'sender':sender}

class ResultsWaitPage(WaitPage):
    #body_text = 'please wait dictator'
    def after_all_players_arrive(self):
        pass




class Results(Page):

    def vars_for_template(self):
        dicshare = 100 - self.group.dg_decision
        receiver = self.group.get_player_by_role('receiver')
        sender = self.group.get_player_by_role('dictator')
        return {
            "receiver": receiver,
            'sender': sender,
            'dictators_share': dicshare}


page_sequence = [
    Intro,
    WaitPage,
    Decision,
    ResultsWaitPage,
    Results
]
