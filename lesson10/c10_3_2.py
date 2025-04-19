from email import message
from email.mime import multipart
from email.mime import text
import smtplib

smtp_host = 'smtp.gmail.com'
smtp_port = 587

from_email = 'hogehoge@gmail.com'
to_email = 'hogehoge@gmail.com'
username = 'hogehoge@gmail.com'
password = 'urgpgscufecyhoeh'

msg = multipart.MIMEMultipart()
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('Test email', 'plain'))

with open('lesson.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='lesson.txt'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
