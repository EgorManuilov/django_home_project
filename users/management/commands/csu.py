from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin_egor@mail.ru',
            first_name='Admin',
            last_name='Egor',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin_egor123')
        user.save()
