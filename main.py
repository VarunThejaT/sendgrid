import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
load_dotenv()

def generate_email_with_sendgrid(to_email_address, otp):

    message = Mail(
        from_email=os.getenv('SENDGRID_FROM_EMAIL'),
        to_emails=to_email_address,
        subject='This a test subject for an otp email',
        html_content=f'Hi, your verification code is: {otp}')
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

generate_email_with_sendgrid("varuntheja.atp@gmail.com", "123123")