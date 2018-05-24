from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    form_model = 'player'
    form_fields = ['gender', 'check']

    def check_error_message(self, value):
        if not value:
            return 'Read intro more carefully and try again.'


class Decision1(Page):
    form_model = 'group'
    form_fields = ['offer']

    def is_displayed(self):
        return self.player.role() == 'agent1'

    def vars_for_template(self):
        agent2 = self.group.get_player_by_role('agent2')
        agent1 = self.group.get_player_by_role('agent1')
        return {
            "agent2": agent2,
            'agent1': agent1}



class Decision2(Page):
    form_model = 'group'
    form_fields = ['yesno']
    timeout_seconds = 15
    timeout_submission = {'yesno': True}


    def is_displayed(self):
        return self.player.role() == 'agent2'

    def vars_for_template(self):
        agent2 = self.group.get_player_by_role('agent2')
        agent1 = self.group.get_player_by_role('agent1')
        return {
            "agent2": agent2,
            'agent1': agent1}



class ResultsWaitPage(WaitPage):
    # body_text = 'please wait dictator'
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    def vars_for_template(self):
        another_player_payoff = self.player.get_others_in_group()[0].payoff
        return {"another_player_payoff": another_player_payoff}


page_sequence = [
    Intro,
    WaitPage,
    Decision1,
    WaitPage,
    Decision2,
    ResultsWaitPage,
    Results
]
