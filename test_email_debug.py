
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load render.env specifically
load_dotenv('render.env')

email_user = os.getenv('EMAIL_HOST_USER')
email_password = os.getenv('EMAIL_HOST_PASSWORD')

print(f"Testing Email Connection...")
print(f"User: {email_user}")
print(f"Password starts with: {email_password[:2]}... (length: {len(email_password)})")

try:
    print("Connecting to smtp.gmail.com:587...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)  # Show SMTP conversation
    
    print("Starting TLS...")
    server.starttls()
    
    print("Logging in...")
    server.login(email_user, email_password)
    print("Login successful!")
    
    # Send test email
    msg = MIMEText("This is a test email from the debugging script.")
    msg['Subject'] = "SMTP Debug Test"
    msg['From'] = email_user
    msg['To'] = email_user # Send to self
    
    print(f"Sending test email to {email_user}...")
    server.sendmail(email_user, [email_user], msg.as_string())
    print("Email sent successfully!")
    
    server.quit()
    
except Exception as e:
    print(f"\nERROR: {e}")
    import traceback
    traceback.print_exc()
