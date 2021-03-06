import smtplib
import getpass
import os
from dotenv import load_dotenv

load_dotenv()

f_name = "Евпатий"
s_name = "Сергей"
subject = "Приглашение!"

ref_link = "https://dvmn.org/referrals/99I26R95e7TOhFwppYNEMUVMvPsOGOCb4aDnxOZY/"
link_tag = r"%website%"
name_tag = r"%friend_name%"
self_name_tag = r"%my_name%"

sender_address = os.getenv("SENDER_DVMN")
receiver_address = os.getenv("RECEIVER_DVMN")

header = f"""From: {sender_address}
To: {receiver_address}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

"""

email_body = "";
with open("mail.txt", 'r', encoding='utf-8') as email_body_txt_file:
    email_body = email_body_txt_file.read()

email_body = email_body.replace(link_tag, ref_link) \
                .replace(name_tag, f_name) \
                .replace(self_name_tag, s_name)


letter = header + email_body
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
password = getpass.getpass(prompt="Enter secret password:")

server.login("svmatveev1988", password)
server.sendmail(sender_address,
                receiver_address,
                letter)
server.quit()