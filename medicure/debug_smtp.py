import smtplib
from django.conf import settings
import os
import django

# Setup Django standalone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicure.settings')
django.setup()

def test_smtp():
    host = settings.EMAIL_HOST
    port = settings.EMAIL_PORT
    user = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD

    print(f"Connecting to {host}:{port}...")
    try:
        server = smtplib.SMTP(host, port)
        server.set_debuglevel(1)  # Show all interactions
        
        print("EHLO...")
        server.ehlo()
        
        if settings.EMAIL_USE_TLS:
            print("STARTTLS...")
            server.starttls()
            print("EHLO (again)...")
            server.ehlo()
        
        print("Logging in...")
        server.login(user, password)
        print("LOGIN SUCCESSFUL!")
        
        msg = f"Subject: SMTP Test\n\nThis is a test email from Python smtplib."
        print("Sending mail...")
        server.sendmail(user, [user], msg)
        print("MAIL SENT!")
        
        server.quit()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    test_smtp()
