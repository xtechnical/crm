from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'


# we made it for signals
    def ready(self):
        import accounts.signals
