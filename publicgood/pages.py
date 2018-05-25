from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class Intro(Page):
    form_model = 'player'
    form_fields =['check']

    def check_error_message(self, value):
        if value:
            return 'Read intro more carefully and try again.'
    pass

class Decision(Page):

    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    body_text = 'please wait others'
    def after_all_players_arrive(self):
        self.group.set_payoffs()




class Results(Page):

    def vars_for_template(self):
        another_player_payoff = self.player.get_others_in_group()[0].payoff
        return {"another_player_payoff": another_player_payoff}

        # total_contribution = sum([p.contribution for p in self.get_players()])
        #
        # individual_share = self.total_contribution * Constants.coefficient / Constants.players_per_group
        # for p in self.get_players():
        #     p.payoff = Constants.endowment - p.contribution + individual_share
        #
        #
        # def set_payoffs(self):
        #     self.total_contribution = sum([p.contribution for p in self.get_players()])
        #     individual_share = self.total_contribution * Constants.coefficient / Constants.players_per_group
        #     for p in self.get_players():
        #         p.payoff = Constants.endowment - p.contribution + individual_share
        #
        # # dicshare = 100 - self.group.dg_decision
        # # player1 = self.group.get_player_by_role('player1')
        # # player2 = self.group.get_player_by_role('player2')
        # # player3 = self.group.get_player_by_role('player3')
        # # player4 = self.group.get_player_by_role('player4')
        #
        # return {
        #     "receiver": receiver,
        #     'sender': sender,
        #     'dictators_share': dicshare}


page_sequence = [
    Intro,
    Decision,
    ResultsWaitPage,
    Results
]
