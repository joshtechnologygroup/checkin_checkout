from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to
import sql_driver

import re


@respond_to('alert (.*)', re.IGNORECASE)
def send__ss_alert(message, name):
    sql = "SELECT UserId, LogDate, Direction FROM DeviceLogs_2_2018 " \
          "where logdate > Convert(datetime, '2018-02-25 17:09:00');"
    data = sql_driver.execute(sql)
    print(data)
    message.reply('Here is %s' % 'in office' if data[0] else 'not yet in office')
