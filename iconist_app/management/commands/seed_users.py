from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with user data'

    def handle(self, *args, **kwargs):
        roles = ['admin', 'sdm', 'spv', 'officer']

        for i in range(10):
            username = f'user{i}'
            email = f'user{i}@example.com'
            role = random.choice(roles)

            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    email=email,
                    password='password123',
                    role=role
                )
                self.stdout.write(self.style.SUCCESS(f'Created user {username} with role {role}'))
            else:
                self.stdout.write(self.style.WARNING(f'User {username} already exists'))
