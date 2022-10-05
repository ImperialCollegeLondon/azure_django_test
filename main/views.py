from django.shortcuts import HttpResponse, render  # noqa: F401


def index(request):
    return HttpResponse("content")


def exception(request):
    raise Exception("a message")
