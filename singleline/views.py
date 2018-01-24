# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.utils.encoding import smart_str, smart_unicode

import requests
import json
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def edit_page(request):
    return render(request, 'hometext.html')


def edit_action(request):
    title = request.POST.get('title')

    url = "http://api.meaningcloud.com/lang-2.0"

    payload = "key=1b2ea248af8252d4d3ef84d0ef6798ce&txt=" + title + "&url=&doc="

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    data = json.loads(response.text)

    language = data['language_list'][0]['name']

    return render(request, 'lang.html', {'language': language})