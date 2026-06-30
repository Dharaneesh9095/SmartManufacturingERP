from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Create default admin user"

    def handle(self, *args, **kwargs):
        username = "admin"
        password = "Admin@12345"
        email = "admin@gmail.com"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS("Admin user created"))
        else:
            self.stdout.write(self.style.SUCCESS("Admin user already exists"))