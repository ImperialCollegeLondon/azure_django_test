import os

from .settings import *  # noqa: F401, F403

DEBUG = False
ALLOWED_HOSTS = [os.environ["WEBSITE_HOSTNAME"]]
SECRET_KEY = os.environ["SECRET_KEY"]
ADMINS = [("Christopher Cave-Ayland", "c.cave-ayland@imperial.ac.uk")]
# MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 15552000
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = "smtp.cc.ic.ac.uk"
EMAIL_PORT = 465
EMAIL_USE_SSL = True

EMAIL_HOST_USER = os.environ["EMAIL_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]

SERVER_EMAIL = "rcs-noreply@imperial.ac.uk"
DEFAULT_FROM_EMAIL = "rcs-noreply@imperial.ac.uk"
