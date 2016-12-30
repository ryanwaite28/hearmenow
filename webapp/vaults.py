# --- --- --- --- --- #
# --- Helper Code --- #
# --- --- --- --- --- #

import os, sys, cgi, random, string, hashlib, json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template import RequestContext
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.decorators.csrf import csrf_protect

# --- #

webapp_dir = os.path.dirname(os.path.abspath(__file__))

ALLOWED_PHOTOS = set(['png', 'jpg', 'jpeg', 'gif'])
ALLOWED_VIDEOS = set(['mp4', 'avi', 'mov', 'webm', 'oog'])
ALLOWED_AUDIO = set(['mp3', 'wav'])

ALLOWED_MEDIA = set(['png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov', 'webm', 'oog' 'mp3', 'wav'])

def allowed_photo(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_PHOTOS

def allowed_video(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_VIDEOS

def allowed_audio(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_AUDIO



def allowed_media(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_MEDIA



# Instance Tuple Variables For Model Classes

OwnerType = (
    ('Account', 'Account'),
    ('Group', 'Group'),
)

PostTypes = (
    ('Text', 'Text'),
    ('Photo', 'Photo'),
    ('Audio', 'Audio'),
    ('Video', 'Video'),
)

ContentType = (
    ('Post', 'Post'),
    ('Comment', 'Comment'),
    ('Reply', 'Reply'),
    ('Group', 'Group'),
    ('Event', 'Event'),
)

AttachmentTypes = (
    ('Photo', 'Photo'),
    ('Audio', 'Audio'),
    ('Video', 'Video'),
)

ItemType = (
    ('Product', 'Product'),
    ('Service', 'Service'),
)

StarType = (
    ('One', 'One'),
    ('Two', 'Two'),
    ('Three', 'Three'),
    ('Four', 'Four'),
    ('Five', 'Five'),
)

# Dictionary of all pages/views for easy and dynamic rendering.
pages = {
    'welcome': 'welcome.html',
    'error': 'error.html',
    'generic': 'generic-1.html',
    'login': 'login.html',
    'signup': 'signup.html'
}

localPaths = {
    'avatars': webapp_dir + '/static/avatars/',
    'backgrounds': webapp_dir + '/static/backgrounds/',
    'avatars_rel': '/static/avatars/',
    'backgrounds_rel': '/static/backgrounds/',
    'images_rel': '/static/img/'
}

# Master Dictionary
masterDICT = {
    'pages': pages,
    'localPaths': localPaths
}
