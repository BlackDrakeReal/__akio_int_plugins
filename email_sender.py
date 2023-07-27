import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        # Set up the SMTP server
        smtp_server = 'smtp.gmail.com'  # Change this if you are using a different provider
        smtp_port = 587
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()

        # Login to the sender's email account
        smtp.login(sender_email, sender_password)

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        body = message
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        smtp.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the SMTP server
        smtp.quit()

        print("Email sent successfully!")

    except Exception as e:
        print("An error occurred while sending the email:", e)

if __name__ == "__main__":
    sender_email = "akioanonymousemail@gmail.com"  # Replace with your email address
    sender_password = "bkjbxwajqxfpdllg"  # Replace with your email password
    receiver_email = input("Email Reciver >> ")  # Replace with the recipient's email address
    subject = input("Object >> ")
    message1 = input("Message >> ")
    message = "Sent From Akio Tool https://akiotool.tk/\n\n"

    send_email(sender_email, sender_password, receiver_email, subject, (message + message1))
