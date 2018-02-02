from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from ..util.URLBuilder import URLBuilder

from django.http import HttpResponse
from django.views import View

import urllib.request

from django.contrib.auth.mixins import LoginRequiredMixin

class LogInView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return redirect(URLBuilder().HOME_URI) #logout of authentication server
