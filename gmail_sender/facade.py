# gmailを使ったメール送信のサンプルプログラム
from smtplib import SMTP
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import emoji

class GmailSender:
    def __init__(self, from_address, password):
        self.from_address = from_address
        self.password = password
        self.mime_dic = {"jpeg": "image",
                         "jpg": "image",
                         "png": "image"}


    def _setMessage(self, to_address, subject, body):

        # メールヘッダー
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.from_address
        msg['To'] = to_address

        # メール本文
        body = MIMEText(body)
        msg.attach(body)
        return msg

    def _setAttach(self, path, msg):
        name = path.split("/")[-1]
        ext = name.split('.')[-1]
        
        # 添付ファイルの設定
        attach_file = {'name': name, 'path': path} # nameは添付ファイル名。pathは添付ファイルの位置を指定
        attachment = MIMEBase(self.mime_dic[ext], ext)
        file = open(attach_file['path'], 'rb+')
        attachment.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=attach_file['name'])
        msg.attach(attachment)
        return msg

    def _send(self, msg): 
        host, port = 'smtp.gmail.com', 587
        gmail=SMTP(host, port)
        gmail.starttls() 
        gmail.login(self.from_address, self.password)
        gmail.send_message(msg)

    def send(self, to_address, subject, body, attach_lst=[]):
        msg = self._setMessage(to_address, subject, body)
        for attach in attach_lst:
            msg = self._setAttach(attach, msg)
        self._send(msg)
        print(emoji.emojize(":envelope: Sent Email. :envelope:"))

