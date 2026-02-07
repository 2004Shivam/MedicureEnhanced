
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicure.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

print("Verifying ALL users...")
for user in User.objects.all():
    if not user.is_verified:
        user.is_verified = True
        user.save()
        print(f"Verified user: {user.email}")
    else:
        print(f"Already verified: {user.email}")

print("Done verifying all users.")
