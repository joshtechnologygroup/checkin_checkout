from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to

import re


@respond_to('send alert to (.*)', re.IGNORECASE)
def send__ss_alert(message, name):
    message.reply('Here is %s' % name)
