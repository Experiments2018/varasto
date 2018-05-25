from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}



SESSION_CONFIGS = [
    # {
    #     'name': 'guess_game_juho',
    #     'display_name': "Guess Game Juho",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['guess_game_juho'],
    # },
    # {
    #     'name': 'dictatorgame_baseline',
    #     'display_name': "Dictator Game - baseline",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['dictatorgame'],
    #     'tgender': False,
    # },
    # {
    #     'name': 'dictatorgame_gender',
    #     'display_name': "Dictator Game - gender info",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['dictatorgame'],
    #     'tgender': True,
    # },
    {
        'name': 'politicalgame',
        'display_name': "Political Game",
        'num_demo_participants': 1,
        'app_sequence': ['politicalgame'],
        'tgender': True,
    },

{
        'name': 'charity',
        'display_name': "Charity Game",
        'num_demo_participants': 1,
        'app_sequence': ['charity'],
        'tgender': True,
    },

{
        'name': 'ultimatumgame_gender',
        'display_name': "Ultimatum Game - gender info",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatumgame'],
        'tgender': True,
    },
{
        'name': 'publicgood',
        'display_name': "Public Goods Game",
        'num_demo_participants': 3,
        'app_sequence': ['publicgood'],
        'tgender': True,
    },
]



# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CHF'
USE_POINTS = True
#POINTS_CUSTOM_NAME = 'Markka'
ROOMS = [
    {
        'name': 'stgallen'
        'display_name': 'Room for St.Gallen',
    },
]


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = 'jt=$nu$^3d6k2=+1ss(ag^rzo&0y9c%p)dx!aa7zn-_2^us#g1'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
