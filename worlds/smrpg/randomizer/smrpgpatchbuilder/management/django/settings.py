# minimal_settings.py

SECRET_KEY = 'dummy'  # Required by Django

INSTALLED_APPS = [
    "smrpgpatchbuilder",  # Must match your folder name in `src/`
]

# Optional: Disable database if unused
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}

# Optional: Timezone support
USE_TZ = False
