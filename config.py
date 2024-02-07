import os

API_ID = API_ID = 20088962

API_HASH = os.environ.get("API_HASH", "257f47d347157555890a64b12bc0134f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6827672847:AAEaVb_pWe4uZBZZSSYnK00Wp-_IT35ulr4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6169016546))

LOG = -1001851582041

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6169016546").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


