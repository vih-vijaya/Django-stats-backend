from django.core.management.base import BaseCommand
from django.utils.timezone import now
from statapp.models import Business
import random

class Command(BaseCommand):
    help = "Generate dummy business data periodically"

    def handle(self, *args, **kwargs):
        company_names = ["Alpha Corp", "Beta Ltd", "Gamma Inc", "Delta Solutions"]
        new_business = Business.objects.create(
            name=random.choice(company_names),
            revenue=random.randint(100000, 1000000),
            profit=random.randint(5000, 200000),
            employees=random.randint(10, 500),
            country=random.choice(["USA", "UK", "India", "Canada"]),
        )
        self.stdout.write(self.style.SUCCESS(f"Added: {new_business.name} at {now()}"))
