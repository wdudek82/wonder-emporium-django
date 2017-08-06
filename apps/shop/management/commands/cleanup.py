from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    There is default django command to do that.
    This is only an example of custom command.
    """
    help = 'Cleans up expired sessions'

    def handle(self, *args, **options):
        """
        code to delete old or anonymous sessions
        """
        self.stdout.write('Successfully cleared sessions')
