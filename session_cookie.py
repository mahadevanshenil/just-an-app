import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Email configuration
    from_email = "letstestinfor@gmail.com"  # Replace with your email address
    password = "qlycliuhijrntnwu"      # Replace with your email password
    smtp_server = "smtp.gmail.com"        # Replace with your SMTP server (e.g., smtp.gmail.com)
    smtp_port = 587

    # Create a MIME text message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

def main():
    # URL of the website to fetch session cookie data
    url = "https://youtube.com"  # Replace with the URL of the website

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract session cookies from the response
        cookies = response.cookies

        # Prepare the email body
        email_body = "Session Cookie Data:\n\n"
        for cookie in cookies:
            email_body += f"Name: {cookie.name}, Value: {cookie.value}\n"

        # Send the email
        subject = "Session Cookie Data"
        send_email(subject, email_body, "mahadevashenil@gmail.com")  # Replace with the recipient's email address
        print("Session cookie data sent to the email.")
    else:
        print(f"Failed to retrieve session cookie data. Status code: {response.status_code}")

if __name__ == "__main__":
    main()



'''You must provide a password because the script acts as an automated email client connecting to an SMTP server, which requires authentication to prove you own the account and to prevent unauthorized spam. Without valid login credentials, email providers like Gmail or Yahoo will immediately reject the connection.
However, you should never type your actual email account password directly into a Python script. Doing so exposes your main password to anyone who views the file.
Here is how to handle email authentication safely:
Generate an App Password: Modern email providers block standard password logins from automated scripts. You need to go to your email security settings (e.g., Google Account > Security > 2-Step Verification > App Passwords) and generate a unique, 16-character password used strictly for this script.
Use Environment Variables: Instead of hardcoding the App Password in plain text (password = "my_app_password"), store it securely on your computer and retrieve it using Python's os module.
To secure your script, import the os module at the top and update the password line to:password = os.environ.get("EMAIL_PASSWORD")'''

'''
To fully test it, you would need to:
Use a real SMTP server and valid credentials.
Change the url to a website that actually sets a cookie on the initial GET request (like a site that sets a guest session ID or a load balancer cookie).
'''