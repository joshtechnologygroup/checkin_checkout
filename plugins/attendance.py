import re
import time

from mattermost_bot.bot import respond_to

import sql_driver


@respond_to('alert (.*)', re.IGNORECASE)
def send__ss_alert(message, name):
    print(name)
    print(time.strftime('%y-%m-%d %H:%M:%S'))

    request_time = time.strftime('%Y-%m-%d')

    get_user_checking_status_sql = "SELECT top(1) UserId, LogDate, Direction FROM DeviceLogs_2_2018 " \
                                   "WHERE userid = (SELECT EmployeeCodeInDevice FROM Employees WHERE EmployeeName = '" + name + "')" \
                                                                                                                                "AND logdate > Convert(datetime, '" + request_time + "') " \
                                                                                                                                                                                     "ORDER BY logdate DESC;"

    if not verify_employee_exist(name):
        message.reply('%s does not work here. At least not that I know of. ' % name)
        return

    request_in_progress = True
    in_progress_message_sent = True

    while request_in_progress:
        data = sql_driver.execute(get_user_checking_status_sql)

        if len(data) > 0 and data[0] is not None:
            data = data[0]
            direction = data[-1]
            if direction.upper() == 'IN':
                message.reply('%s is in office' % name)
                request_in_progress = False
            elif direction.upper() == 'OUT':
                message.reply('%s has left' % name)
                request_in_progress = False
        else:
            if in_progress_message_sent:
                message.reply('%(name)s has not yet arrived in office. '
                              'I\'ll let you know when %(name)s arrive ' % {'name': name})
                in_progress_message_sent = False
        time.sleep(10)


def verify_employee_exist(employeeName):
    verify_employee_exists_sql = "select EmployeeName FROM Employees " \
                                 "WHERE EmployeeName = '" + employeeName + "';"
    check_name_data = sql_driver.execute(verify_employee_exists_sql)
    if len(check_name_data) > 0 and check_name_data[0] is not None:
        return True
    else:
        return False
