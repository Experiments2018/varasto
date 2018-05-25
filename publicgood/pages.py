from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    form_model = 'player'
    form_fields = ['check']

    def check_error_message(self, value):
        if value:
            return 'Read intro more carefully and try again.'

    def is_displayed(self):
        if self.round_number == 1:
            return True

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
        data = [p.payoff for p in self.group.get_players()]
        totalcontribs = [round(g.total_contribution/Constants.players_per_group) for g in self.group.in_all_rounds()]
        yourcontr = [y.contribution for y in self.player.in_all_rounds()]

        series = [{
            'name': 'Your contribution per round',
            'type': 'column',
            'data': yourcontr,

        },
            {
                'name': 'Average contributions per round',
                'type': 'line',
                'data': totalcontribs,
            }
        ]
        return {'series': series}

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


class Finalresults(Page):

    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True

    pass


page_sequence = [
    # Intro,
    Decision,
    ResultsWaitPage,
    Results,
    Finalresults

]
