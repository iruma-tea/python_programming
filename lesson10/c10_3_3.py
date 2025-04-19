import logging
import logging.handlers


smtp_host = 'smtp.gmail.com'
smtp_port = 587

from_email = 'hogehoge@gmail.com'
to_email = 'hogehoge@gmail.com'
username = 'hogehoge@gmail.com'
password = 'urgpgscufecyhoeh'

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

logger.info('test')
logger.critical('critical')
