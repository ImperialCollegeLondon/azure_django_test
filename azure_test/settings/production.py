import os

from .settings import *  # noqa: F401, F403

DEBUG = False
ALLOWED_HOSTS = [os.environ["WEBSITE_HOSTNAME"]]
SECRET_KEY = os.environ["SECRET_KEY"]

ADMINS = [("Christopher Cave-Ayland", "c.cave-ayland@imperial.ac.uk")]
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")  # noqa: F405
SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 15552000

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# assume we are deploying within College network
EMAIL_HOST = "smarthost.cc.ic.ac.uk"
SERVER_EMAIL = "noreply@imperial.ac.uk"
