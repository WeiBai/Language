#coding: utf-8
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import requests
import json
import detectlanguage

def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfiles = request.FILES['myfile']
        fs = FileSystemStorage()

        filename = fs.save(myfiles.name, myfiles)

        uploaded_file_url = fs.path(filename)

        input_file = open(uploaded_file_url, "r+")

        input_str = input_file.read(50);

        url = "http://api.meaningcloud.com/lang-2.0"

        payload = "key=1b2ea248af8252d4d3ef84d0ef6798ce&txt=" + input_str + "&url=&doc="

        # print payload

        headers = {'content-type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, data=payload, headers=headers)

        data = json.loads(response.text)

        language = data['language_list'][0]['name']

        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'lang': language
        })
    return render(request, 'upload.html')


def detectlanguage(input_string):
    detectlanguage.configuration.api_key = "7750ba3cec7607c4e9a95584b94bb464"
    result = detectlanguage.detect("Good Morning")
