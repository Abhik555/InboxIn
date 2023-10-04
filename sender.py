import smtplib


smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'inboxin40@gmail.com'
sender_password = 'fgjl kkfg ioax ptxr'

# Read recipient email addresses from a text file
recipient_emails = []
with open('recipient_emails.txt', 'r') as file:
    recipient_emails = [line.strip() for line in file]

# Compose the email
subject = 'This email was sent by InboxIN'
message = '''This is a trial email done for error checking.
           Thank you for your support'''

# Connect to the SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
except Exception as e:
    print(f"Error: {e}")
    exit()

# Send the email to recipients from the text file
for recipient_email in recipient_emails:
    try:
        server.sendmail(sender_email, recipient_email, f'Subject: {subject}\n\n{message}')
        print(f'Email sent successfully to {recipient_email}!')
    except Exception as e:
        print(f"Error: {e}")

# Quit the SMTP server
server.quit()
