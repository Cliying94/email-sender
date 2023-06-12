import email.message
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import csv


load_dotenv()

ACCOUNT = os.getenv("ACCOUNT")
PASSWORD = os.getenv("PASSWORD")
email_title = "Email title"

with open('email-list-test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0])
        msg=email.message.EmailMessage()
        msg["From"]=ACCOUNT
        msg["Bcc"] = row[0]  # Replace with the appropriate column index in your CSV file
        msg["Subject"]= email_title
    
        # Open and read the HTML file
        with open('html_content.html', 'r') as file:
            html_content = file.read()
    
        # # Create a MIMEText object with the HTML content
        # html_part = MIMEText(html_content, subtype="html")
    
        msg.add_alternative(html_content, subtype="html")
    
        import smtplib
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(ACCOUNT,PASSWORD)
            server.send_message(msg)
