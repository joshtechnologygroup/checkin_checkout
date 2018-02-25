import time
from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to
from retrying import retry

import sql_driver

import re

@respond_to('alert (.*)', re.IGNORECASE)
def send__ss_alert(message, name):
    print(name)
    print(time.strftime('%y-%m-%d %H:%M:%S'))
    lol = time.strftime('%Y-%m-%d')
    sql = "select top(1) UserId, LogDate, Direction FROM DeviceLogs_2_2018 " \
          "WHERE userid = (select EmployeeCodeInDevice from Employees where EmployeeName = '"+ name +"')" \
          "AND logdate > Convert(datetime, '" + lol + "') " \
          "order by logdate desc;"

    flag = True
    flag2 = True
    retries = 1
    while flag:
        print(name + " - " + str(retries++))
        data = foo(sql)
        print(data)

        if len(data) > 0 and data[0] is not None:
            data = data[0]
            direction = data[-1]
            if direction.upper() == 'IN':
                message.reply('%s is in office' % name)
                flag = False
            elif direction.upper() == 'OUT':
                message.reply('%s has left' % name)
                flag = False
        else:
            if flag2:
                message.reply('%s has not yet arrived in office' % name)
                flag2 = False
        time.sleep(10)


@retry(stop_max_attempt_number=10, wait_random_min=1000, wait_random_max=2000)
def foo(sql):
    return sql_driver.execute(sql)