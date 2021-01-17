# -*- coding: utf-8 -*-
import os, time

# create log dir
if not os.path.isdir('./log'):
    os.mkdir('./log')

# put log
def put_log_msg(str, type):
    if not str or not type:
        print ("logger error")
        return False

    msg = ''
    pMsg = ''

    # open log file
    f = './log/' + time.strftime("%Y-%m-%d", time.localtime()) + '.log'
    fLog = open(f, 'a')

    msg = time.strftime("%H:%M:%S", time.localtime()) + '] ' + str

    if (type == 1):
        msg = '[INFO] [' + msg
        pMsg = '\033[0;32;40m ' + msg

    elif type == 2:
        msg = '[WARNING] [' + msg
        pMsg = '\033[0;33;40m ' + msg

    elif type == 3:
        msg = '[ALERT] [' + msg
        pMsg = '\033[0;35;40m ' + msg

    elif type == 4:
        msg = '[ERROR] [' + msg
        pMsg = '\033[0;31;40m ' + msg

    elif type == 5:
        msg = '[SUCCESS] [' + msg
        pMsg = '\033[0;37;40m ' + msg
    else:
        print ("type error!")
        fLog.close()
        return False

    print (pMsg)

    fLog.write(msg + '\n')
    fLog.close()

    pass
