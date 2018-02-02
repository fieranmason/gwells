from django.contrib.auth.middleware import get_user
from django.utils.functional import SimpleLazyObject
from pprint import pprint
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class GWellsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("GWellsMiddleware __call__ function");
        return self.get_response(request)
