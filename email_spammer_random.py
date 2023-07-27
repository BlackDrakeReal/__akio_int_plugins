import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

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

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

random_string = generate_random_string(10)

if __name__ == "__main__":
    sender_email = "akioanonymousemail@gmail.com"  # Replace with your email address
    sender_password = "bkjbxwajqxfpdllg"  # Replace with your email password
    receiver_email = input("Email To Spam >> ")  # Replace with the recipient's email address
    subject = random_string
    message1 = random_string
    message = "Sent From Akio Tool https://akiotool.tk/\n\n"

    times_send = input("Enter the number of times to send: ")

    # Convert the user input to an integer
    times_send = int(times_send)

    if times_send > 50:
        print("You can't send more than 50 times.")
    elif times_send < 1:
        print("You can't send less than 1 time.")
    else:
        # The value is between 1 and 50, so you can proceed with the action
        print(f"Sending the email {times_send} times...")
        for i in range(times_send):
            generate_random_string()
            send_email(sender_email, sender_password, receiver_email, subject, (message + message1))
            if i < times_send - 1:
                delay_time = 0.2  # Adjust this value to set the desired delay in seconds between emails
                time.sleep(delay_time)
