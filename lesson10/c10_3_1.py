from email import message
import smtplib

smtp_host = 'smtp.gmail.com'
smtp_port = 587

from_email = 'hogehoge@gmail.com'
to_email = 'hogehoge@gmail.com'
username = 'hogehoge@gmail.com'
password = 'urgpgscufecyhoeh'

msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
