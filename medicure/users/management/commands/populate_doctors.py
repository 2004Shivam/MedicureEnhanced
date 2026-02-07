"""
Management command to populate sample doctors for testing.
All doctors are created as UNAPPROVED - admin must approve them manually.
"""
import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from doctors.models import DoctorProfile

User = get_user_model()

SAMPLE_DOCTORS = [
    {
        "first_name": "Rajesh",
        "last_name": "Sharma",
        "specialization": "Cardiologist",
        "experience": 15,
        "license_number": "MCI-2009-12345",
    },
    {
        "first_name": "Priya",
        "last_name": "Patel",
        "specialization": "Dermatologist",
        "experience": 8,
        "license_number": "MCI-2016-23456",
    },
    {
        "first_name": "Amit",
        "last_name": "Verma",
        "specialization": "Neurologist",
        "experience": 12,
        "license_number": "MCI-2012-34567",
    },
    {
        "first_name": "Sneha",
        "last_name": "Gupta",
        "specialization": "Pediatrician",
        "experience": 6,
        "license_number": "MCI-2018-45678",
    },
    {
        "first_name": "Vikram",
        "last_name": "Singh",
        "specialization": "Orthopedic Surgeon",
        "experience": 20,
        "license_number": "MCI-2004-56789",
    },
    {
        "first_name": "Ananya",
        "last_name": "Reddy",
        "specialization": "Gynecologist",
        "experience": 10,
        "license_number": "MCI-2014-67890",
    },
    {
        "first_name": "Suresh",
        "last_name": "Kumar",
        "specialization": "General Physician",
        "experience": 25,
        "license_number": "MCI-1999-78901",
    },
    {
        "first_name": "Kavita",
        "last_name": "Iyer",
        "specialization": "Psychiatrist",
        "experience": 7,
        "license_number": "MCI-2017-89012",
    },
    {
        "first_name": "Arjun",
        "last_name": "Nair",
        "specialization": "ENT Specialist",
        "experience": 5,
        "license_number": "MCI-2019-90123",
    },
    {
        "first_name": "Meera",
        "last_name": "Joshi",
        "specialization": "Ophthalmologist",
        "experience": 11,
        "license_number": "MCI-2013-01234",
    },
]


class Command(BaseCommand):
    help = 'Populates the database with 10 sample doctors (all unapproved)'

    def handle(self, *args, **options):
        created_count = 0
        skipped_count = 0

        for doctor_data in SAMPLE_DOCTORS:
            email = f"dr.{doctor_data['first_name'].lower()}.{doctor_data['last_name'].lower()}@medicure.demo"
            username = f"dr_{doctor_data['first_name'].lower()}_{doctor_data['last_name'].lower()}"

            # Check if user already exists
            if User.objects.filter(email=email).exists():
                self.stdout.write(self.style.WARNING(f"Skipped: {email} already exists"))
                skipped_count += 1
                continue

            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password="DemoDoctor@123",  # Default password for testing
                first_name=doctor_data['first_name'],
                last_name=doctor_data['last_name'],
                is_doctor=True,
                is_patient=False,
                is_verified=True,  # Email verified so they can login
            )

            # Create doctor profile (UNAPPROVED)
            DoctorProfile.objects.create(
                user=user,
                specialization=doctor_data['specialization'],
                experience=doctor_data['experience'],
                license_number=doctor_data['license_number'],
                is_approved=False,  # NOT approved - admin must approve
            )

            self.stdout.write(self.style.SUCCESS(
                f"Created: Dr. {doctor_data['first_name']} {doctor_data['last_name']} "
                f"({doctor_data['specialization']}, {doctor_data['experience']} yrs) - UNAPPROVED"
            ))
            created_count += 1

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(f"✅ Created {created_count} doctors"))
        if skipped_count:
            self.stdout.write(self.style.WARNING(f"⚠️ Skipped {skipped_count} (already exist)"))
        self.stdout.write(self.style.NOTICE("📋 All doctors are UNAPPROVED. Go to Admin Panel to approve them."))
