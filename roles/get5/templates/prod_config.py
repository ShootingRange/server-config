
##### You must change these before running
SQLALCHEMY_DATABASE_URI = '{{ get5.database }}'  # Sqlalchemy database connection info
STEAM_API_KEY = '{{ get5.steam_api_key }}'  # See https://steamcommunity.com/dev/apikey
SECRET_KEY = '{{ get5.secret_key }}'  # Secret key used for flask cookies
DATABASE_KEY = '{{ get5.database_key }}'  # Used for encryption on database. MUST BE 16 BYTES.
WEBPANEL_NAME = 'Coolshop GGW - Get5' # Used for the title header on the webpage.
JSON_AS_ASCII = False #UTF-8 Encoding Issue.
CUSTOM_PLAYER_NAMES = True
##### Everything below this line is optional to change

import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), '..', 'logs'))
LOG_PATH = os.path.join(location, 'get5.log')

DEBUG = False
TESTING = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
USER_MAX_SERVERS = 10  # Max servers a user can create
USER_MAX_TEAMS = 100  # Max teams a user can create
USER_MAX_MATCHES = 1000  # Max matches a user can create
USER_MAX_SEASONS = 100 # Max seasons a user can create
DEFAULT_PAGE = '/matches'
ADMINS_ACCESS_ALL_MATCHES = True  # Whether admins can always access any match admin panel
CREATE_MATCH_TITLE_TEXT = True # Whether settings for "match title text" and "team text" appear on "create a match page"

# All maps that are selectable in the "create a match" page
MAPLIST = [
    'de_dust2',
    'de_inferno',
    'de_mirage',
    'de_nuke',
    'de_overpass',
    'de_train',
    'de_vertigo',
    'de_season',
    'de_cbble',
    'de_cache',
]

# Maps whose checkbox is selected (in the mappool) by default in the "create a match" page
DEFAULT_MAPLIST = [
    'de_dust2',
    'de_inferno',
    'de_mirage',
    'de_nuke',
    'de_overpass',
    'de_train',
    'de_vertigo',
]

# You may set the game server to allow whitelisted steam ids to specatate.
# By default, NO users can spectate matches.
# Change [] out with your own SteamID. Example ["STEAMID64"]
SPECTATOR_IDS = []

# You may set the server to allow allow whitelisted steamids to login.
# By default any user can login and create teams/servers/matches.
# Change [] out with your own SteamID. Example ["STEAMID64"]
WHITELISTED_IDS = []

# Admins will have extra access to create "public" teams, and if ADMINS_ACCESS_ALL_MATCHES
# is set, they can access admin info for all matches (can pause, cancel, etc.) ANY match.
# Change [] out with your own SteamID. Example ["STEAMID64"]
ADMIN_IDS = []

# Super admins will have the most access, as if ADMINS_ACCESS_ALL_MATCHES was set.
# They'll be able to access EVERYTHING for ANY match, as well as FORFEIT matches.
# Change [] out with your own SteamID. Example ["STEAMID64"]
SUPER_ADMIN_IDS = [
]
