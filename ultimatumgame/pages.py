from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    form_model = 'player'
    form_fields = ['gender']

class Decision1(Page):
    form_model = 'group'
    form_fields = ['offer']

    def is_displayed(self):
        return self.player.role() == 'agent1'

    def vars_for_template(self):
        agent2 = self.group.get_player_by_role('agent2')
        agent1 = self.group.get_player_by_role('agent1')
        return {
                "agent2":agent2,
                'agent1':agent1}

class ResultsWaitPage(WaitPage):
    #body_text = 'please wait dictator'
    def after_all_players_arrive(self):
        pass


class Decision2(Page):
    form_model = 'group'
    form_fields = ['yesno']

    def is_displayed(self):
        return self.player.role() == 'agent2'

    def vars_for_template(self):
        agent2 = self.group.get_player_by_role('agent2')
        agent1 = self.group.get_player_by_role('agent1')
        return {
                "agent2":agent2,
                'agent1':agent1}


class Results(Page):

    # vars_for_template(self):
    #    offer = self.group.dg_decision
     #   receiver = self.group.get_player_by_role('receiver')
      #  sender = self.group.get_player_by_role('dictator')
       # return {
        #    "receiver": receiver,
         #   'sender': sender,
          #  'dictators_share': dicshare}


    pass


page_sequence = [
    Intro,
    WaitPage,
    Decision1,
    WaitPage,
    Decision2,
    ResultsWaitPage,
    Results
]
