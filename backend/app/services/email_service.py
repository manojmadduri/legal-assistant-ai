import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..config import settings

def send_email(subject: str, recipient: str, body: str):
    msg = MIMEMultipart()
    msg['From'] = "your_legal_assistant@example.com"
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email@example.com', settings.EMAIL_API_KEY)
        server.sendmail(msg['From'], recipient, msg.as_string())
        server.quit()
        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"error": str(e)}
