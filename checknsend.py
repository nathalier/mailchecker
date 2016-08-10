__author__ = 'Nathalie'

import imaplib
import datetime

MAIL_ACCOUNT = 'me@gmail.com'
MAIL_PASS = 'pass'
FOLDER = '[Gmail]/All Mail'
OK_CODE = 'OK'

def send_alert():
    pass

M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    M.login(MAIL_ACCOUNT, MAIL_PASS)
except imaplib.IMAP4.error:
    import sys
    print ('Login to the mailbox failed. Please, check credentials.')
    sys.exit('Login failed')

res, data = M.select(FOLDER)
if res != OK_CODE:
    print("Unable to open folder: ", res)
else:
    # res, msgnums = mail.search(None, '(SENTON "09-Aug-2016")')
    res, msgnums = M.search(None, \
                '(SENTON "' + (datetime.date.today() - datetime.timedelta(days=1)).strftime('%d-%b-%Y') + '")')
    if res != OK_CODE:
        print("Error occured: ", res)
    else:
        if len(msgnums) < 1 or len(msgnums) == 1 and len(msgnums[0]) == 0:
            send_alert()
M.close()
M.logout()
