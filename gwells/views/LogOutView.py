from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from ..util.URLBuilder import URLBuilder

from django.http import HttpResponse
from django.views import View

import urllib.request

class LogOutView(View):

    def get(self, request, *args, **kwargs):
        logout(request) #logout of django
        urllib.request.urlopen("https://logon.gov.bc.ca/clp-cgi/logoff.cgi").read()
        return redirect(URLBuilder().LOGOUT_URI) #logout of authentication server
