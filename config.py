from qwebirc.config_options import *
IRCSERVER, IRCPORT = "127.0.0.1", 6667
REALNAME = ""
IDENT = "Chat"
WEBIRC_MODE = None
BASE_URL = ""
NETWORK_NAME = ""
APP_TITLE = "My Libre Cam"

# Tips and bitcoin (CHANGE) install electrum and copy one address

BITCOIN="13rwX3iWNmAqkRyRyUDDBq3cARS1izkkXK"
BITCOIN_MSG="Bitcoin"

TIP="Send Tips"
TIP0="bitcoin://"+BITCOIN+"&amount=.006"
TIP0_MSG="Kiss me"
TIP1="bitcoin://"+BITCOIN+"&amount=0.01"
TIP1_MSG="Touch me"
TIP2="bitcoin://"+BITCOIN+"&amount=0.015"
TIP2_MSG="Stroke me"
TIP3="bitcoin://"+BITCOIN+"&amount=0.125"
TIP3_MSG="Fuck me"

NICKNAME_VALIDATE = True

import string
NICKNAME_VALID_FIRST_CHAR = string.letters + "_[]{}`^\\|"
NICKNAME_VALID_SUBSEQUENT_CHARS = NICKNAME_VALID_FIRST_CHAR + string.digits + "-"
NICKNAME_MINIMUM_LENGTH = 2
NICKNAME_MAXIMUM_LENGTH = 15
FEEDBACK_FROM = "moo@moo.com"
FEEDBACK_TO = "moo@moo.com"

FEEDBACK_SMTP_HOST, FEEDBACK_SMTP_PORT = "127.0.0.1", 25
ADMIN_ENGINE_HOSTS = ["127.0.0.1"]
UPDATE_FREQ = 0.5

MAXBUFLEN = 100000
MAXSUBSCRIPTIONS = 1
MAXLINELEN = 600
DNS_TIMEOUT = 5

HTTP_AJAX_REQUEST_TIMEOUT = 30
HTTP_REQUEST_TIMEOUT = 5

STATIC_BASE_URL = ""
DYNAMIC_BASE_URL = ""

CONNECTION_RESOLVER = None
HMACKEY = "mrmoo"
HMACTEMPORAL = 30

AUTHGATEDOMAIN = "webchat_test"
QTICKETKEY = "boo"

AUTH_SERVICE = "Q!TheQBot@CServe.quakenet.org"
AUTH_OK_REGEX = "^You are now logged in as [^ ]+\\.$"

import dummyauthgate as AUTHGATEPROVIDER

# NO CHANGE!!! - autogenerated
WEBCAM="http://gln7dm4pgfzax5hc.onion:81/cam.mjpg"
AUDIO="http://gln7dm4pgfzax5hc.onion:82/audio.ogg"