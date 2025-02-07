import smtplib
from email.message import EmailMessage

def send_email(news_list):
    EMAIL_ADDRESS = 'your_email@example.com'
    EMAIL_PASSWORD = 'your_password'

    msg = EmailMessage()
    msg['Subject'] = 'Hearsay: Government Crypto News Update'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'recipient@example.com'

    content = ''
    for article in news_list:
        content += f"{article['title']}\n{article['link']}\n\n"
    msg.set_content(content)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)