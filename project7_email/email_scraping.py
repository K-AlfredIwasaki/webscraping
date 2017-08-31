#!/usr/bin/env python

import sys
import imaplib
import getpass
import email
import datetime
import os
import configparser

config = configparser.ConfigParser()
config.sections()
config.read(r'C:\Users\K\Desktop\0_Master Files\app-config.ini')
config_email = config['UMICH']['email']
config_password = config['UMICH']['pass']


def process_mailbox(M):
    """
    Do something with emails messages in the folder.  
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print ("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print ("ERROR getting message", num)
            return

        print ("\n")
        print ("\n")

        print (data[0][1])
        msg = email.message_from_bytes(data[0][1])
        decode = email.header.decode_header(msg['Subject'])[0]
        subject = str(decode[0])
        print ('Message %s: %s' % (num, subject))
        print ('Raw Date:', msg['Date'])
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            print ("Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S"))


M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    rv, data = M.login(config_email, config_password)
except imaplib.IMAP4.error:
    print ("LOGIN FAILED!!! ")
    sys.exit(1)

print (rv, data)

rv, mailboxes = M.list()
if rv == 'OK':
    print ("Mailboxes:")
    print (mailboxes)

rv, data = M.select("Inbox")
if rv == 'OK':
    print ("Processing mailbox...\n")
    process_mailbox(M)
    M.close()
else:
    print ("ERROR: Unable to open mailbox ", rv)

M.logout()