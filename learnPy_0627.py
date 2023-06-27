# print("ロギング#############")
import logging

# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename='test.log', level=logging.INFO)
# formatter = '%(levelname)s:%(messsage)'


# ロギングのメッセージをカスタマイズする
# formatter = '%(asctime)s:%(message)s'
# logging.basicConfig(level=logging.INFO, format=formatter)

# """
# デフォルトは
# ・クリティカル
# ・エラー
# ・ワーニング
#
# 開発中はそれ以下のログも含めて開発すると便利になる
# ・インフォ
# ・デバッグ
# """

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# logging.info('info {}'.format('test'))
# 古い
# logging.info('info %s' % ('test'))
# logging.info('info %s %s' % ('test', 'test2'))
# logging.info('info %s %s', 'test', 'test2')

print("ロガー#############")
# import logging
# logging.basicConfig(level=logging.INFO)

# logging.info('info')
# logger = logging.getLogger(__name__)
# logger.info('from main')
# logger.setLevel(logging.DEBUG)
# logger.debug('debug')

# class NoPassFilter(logging.Filter):
#     def filter(self, record):
#         log_message = record.getMessage()
#         return 'password' not in log_message
#
# logger = logging.getLogger(__name__)
# logger.addFilter(NoPassFilter())
# logger.info('from main')
# logger.info('from main password = "test"')
#
# print("ロギングコンフィグ#############")
# logging.config.filter('logging.ini')
# logger = logging.getLogger(__name__)
# logger.addFilter(NoPassFilter())
# logger.info('from main')
# logger.info('from main password = "test"')

# import logging
#
# logger = logging.getLogger(__name__)
#
# logger.error('Api call is failed')
#
# logger.error({
#     'action': 'create',
#     'status': 'fail',
#     'message': 'Api call is failed'
# })

from email import message
from email.mime import multipart
from email.mime import text
import smtplib

smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxx@hotmail.com'
to_email = 'xxx@hotmail.com'

username =  'xxx@hotmail.com'
password =  'dsifvoifjv'

# msg = message.EmailMessage()
msg = multipart.MIMEMultipart()
# msg.set_content('Test email')

msg.attach(text.MIMEText('Test email', 'plain'))

with open('lesson.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename = 'lesson.txt'
    )
    msg.attach(attachment)

msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['to'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()








