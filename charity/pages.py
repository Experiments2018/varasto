from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


import random


class MyPage(Page):

    form_model = 'player'
    form_fields = ['charity_donation', 'don1', 'don2']

    timeout_seconds = 15
    def before_next_page(self):
        if self.timeout_happened:
            self.player.don1 = random.randint(Constants.r_min, self.player.endowment)
            self.player.don2 = self.player.endowment - self.player.don1


    def vars_for_template(self):
        if self.player.personal_A:
            image1 = "valas.jpg"
        else:
            image1 = "greenlogo.png"
        if self.player.personal_B:
            image2 = "sprperson.jpg"
        else:
            image2 = "spr.png"

        return {'image_1': image1,
                    'image_2': image2,}

    def don1_max(self):
            return self.player.endowment

    def don2_max(self):
            return self.player.endowment

    def error_message(self, values):
        print('values is', values)
        if values["don1"] + values["don2"] != self.player.endowment:

            return 'The numbers must add up to {}.'.format(self.player.endowment)



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
