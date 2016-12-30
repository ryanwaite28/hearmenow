# --- --- --- --- #
# --- Imports --- #
# --- --- --- --- #

import os, sys, cgi, random, string, hashlib, json
import webapp

from django.db.models import Q
from django.utils import timezone
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.decorators.csrf import csrf_protect

import vaults
from vaults import masterDICT

# --- ----- --- #
# --- Views --- #
# --- ----- --- #

def welcome(request):
    if request.method == 'GET':
        if 'username' in request.session:
            return redirect('/main/')
        else:
            return render(request, masterDICT['pages']['welcome'])

# ---
