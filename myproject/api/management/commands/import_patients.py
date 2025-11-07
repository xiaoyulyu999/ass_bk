from django.core.management.base import BaseCommand
import pandas as pd
from api.models import Patient
import os

class Command(BaseCommand):
    help = "Import patient data from a CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            type=str,
            help='Path to the CSV file',
            default='api/data/samples.csv'
        )

    def handle(self, *args, **options):
        path = options['path']
        if not os.path.exists(path):
            self.stderr.write(self.style.ERROR(f"File not found: {path}"))
            return

        df = pd.read_csv(path)
        required_fields = [
            "first_name", "last_name", "age", "gender", "date_of_birth", "address", "email",
            "emergency_contact_name", "emergency_contact_phone", "phone_number",
            "insurance_provider", "insurance_number", "diagnosis"
        ]
        missing = [col for col in required_fields if col not in df.columns]
        if missing:
            self.stderr.write(self.style.ERROR(f"Missing columns: {missing}"))
            return

        for _, row in df.iterrows():
            Patient.objects.update_or_create(
                email=row["email"],  # use email as unique key
                defaults={col: row[col] for col in required_fields if col != "email"}
            )

        self.stdout.write(self.style.SUCCESS("✅ CSV imported successfully!"))
