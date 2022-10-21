from logging import getLogger

from django.shortcuts import HttpResponse, render  # noqa: F401

logger = getLogger("django")


def index(request):
    return HttpResponse("content")


def exception(request):
    try:
        raise Exception("a message")
    except Exception:
        logger.exception("an error occured")
        raise
