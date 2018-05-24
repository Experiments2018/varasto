from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


import random


class MyPage(Page):

    form_model = 'player'
    form_fields = ['yrside', "yrscale"]
    def vars_for_template(self):
        if self.player.radical:
            return {'party_image_1': "suom.jpg",
                'party_image_2': "vas.jpg"}

        else:
            return {'party_image_1': "sdp.jpg",
                    'party_image_2': "myimage.png"}


    def yrside_choices(self):
        #rand = random.choice([False, True])
        if self.player.radical:
            choices =["PerusSuomalaiset","Vasemmistoliitto"]
        else:
            choices = ["Kokoomus", "SDP"]
        return choices



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
