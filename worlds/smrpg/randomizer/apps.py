from django.apps import AppConfig


class RandomizerConfig(AppConfig):
    name = 'randomizer'

    def ready(self):
        # Import debug module to register autoreload watcher for config.yml
        from randomizer import debug  # noqa: F401
