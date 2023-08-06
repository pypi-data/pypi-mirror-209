#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import datetime
from time import sleep
import logging
from collections import deque
import smtplib
import email
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from imapclient import IMAPClient


logger = logging.getLogger(__name__)


class MailFetcher:
    """
    Fetch emails from mail inbox using IMAP protocol.
    Usage:

    from xenoslib.mail import MailFetcher
    for email_data in MailFetcher(imap_server, mail_addr, mail_pwd, interval=30, days=30):
        print(email_data["subject"])
    """

    msg_ids = deque(maxlen=999)

    def __new__(cls, imap_server, mail_addr, mail_pwd, interval=30, days=1):
        self = super().__new__(cls)
        self.imap_server = imap_server
        self.mail_addr = mail_addr
        self.mail_pwd = mail_pwd
        self.days = days
        return self.fetching(interval=interval)

    def fetching(self, interval=30):
        """Continuously fetch emails at the specified interval."""
        logger.debug("Start checking emails...")
        while True:
            try:
                yield from self.parse_emails(self.fetch_emails())
            except Exception as exc:
                logger.warning(exc)
            sleep(interval)

    def parse_emails(self, emails):
        for msg_id, msg in emails.items():
            if msg_id in self.msg_ids:
                continue
            body = email.message_from_bytes(msg[b"BODY[]"])
            subject = str(email.header.make_header(email.header.decode_header(body["Subject"])))
            sender = body["From"]
            date = body["Date"]
            payload = body.get_payload(decode=True)
            if payload:
                payload = payload.decode()
            internal_date = msg[b"INTERNALDATE"]
            email_data = {
                "body": body,
                "subject": subject,
                "payload": payload,
                "date": date,
                "sender": sender,
                "internal_date": internal_date,
            }
            yield email_data
            self.msg_ids.append(msg_id)

    def fetch_emails(self):
        """Login and fetch emails."""
        logger.debug(f"Fetching emails from the past {self.days} day(s)...")
        date_str = datetime.datetime.today() - datetime.timedelta(days=self.days)
        with IMAPClient(self.imap_server, timeout=30) as client:
            client.login(self.mail_addr, self.mail_pwd)
            client.select_folder("INBOX", readonly=True)
            messages = client.search(["SINCE", date_str])
            emails = client.fetch(messages, ["INTERNALDATE", "BODY.PEEK[]"])
            return emails


class SMTPMail:
    def __init__(self, smtp_server="", sender="", pasword="", smtp_port=25):
        self.smtp_server = smtp_server
        self.smtp_port = int(smtp_port)
        self.sender = sender
        self.pasword = pasword
        if self.smtp_port == 25:
            self.SMTP = smtplib.SMTP
        else:
            self.SMTP = smtplib.SMTP_SSL

    def send(self, subject, message, receiver=[], cc=[], bcc=[], filename=None):
        msg = MIMEMultipart()
        msg["Subject"] = Header(subject, "utf-8")
        msg["From"] = Header(self.sender, "utf-8")
        msg["To"] = ";".join(receiver)
        msg["Cc"] = ";".join(cc)
        receiver.extend(cc)
        receiver.extend(bcc)
        msg.attach(MIMEText(message, "html", "utf-8"))

        if filename:
            attachment = MIMEApplication(open(filename, "rb").read())
            attachment.add_header("Content-Disposition", "attachment", filename=filename)
            msg.attach(attachment)

        smtp = self.SMTP(self.smtp_server, self.smtp_port)
        try:
            smtp.login(self.sender, self.pasword)
        except Exception as exc:
            print(exc)
            return False
        smtp.sendmail(self.sender, receiver, msg.as_string())
        smtp.quit()
        return True


def test_imap():
    try:
        import env  # noqa
    except ModuleNotFoundError:
        pass
    imap_server = os.environ["imap_server"]
    mail_addr = os.environ["imap_addr"]
    mail_pwd = os.environ["imap_pass"]
    for email_data in MailFetcher(imap_server, mail_addr, mail_pwd, interval=1, days=30):
        print(email_data["subject"])


def test():
    try:
        import env  # noqa
    except ModuleNotFoundError:
        pass
    mail_addr = os.environ["SMTP_ADDR"]
    mail_pwd = os.environ["SMTP_PASS"]
    smtp_server = os.environ["SMTP_SERVER"]
    mail = SMTPMail(smtp_server, sender=mail_addr, pasword=mail_pwd, smtp_port=465)
    mail.send(subject="test", message="test mail", receiver=[os.environ["RECEIVER"]])


if __name__ == "__main__":
    test()
