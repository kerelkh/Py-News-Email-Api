import smtplib
import ssl
import dotenv
import os
import certifi
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


dotenv.load_dotenv()


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv('EMAIL')
    password = os.getenv('EMAIL_PASSWORD')

    receiver = username
    context = ssl.create_default_context(cafile=certifi.where())

    subject = message['title']

    link = message['url']
    body = f"""
{message['description']}

Check full article here:
{link}
"""

    message = MIMEMultipart()
    message['From'] = username
    message['To'] = username
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain', 'utf-8'))
    
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message.as_string())
            server.quit()
    except Exception as e:
        print(e)

