import os
import requests
import json

'''This program detects the language of text files in current directory,
the suffix of the file is .txt'''

arr_txt = [x for x in os.listdir('./') if x.endswith(".txt")]

for file_name in arr_txt:
    single_file = open(file_name, "r+")
    input_str = single_file.read(50);

    url = "http://api.meaningcloud.com/lang-2.0"

    payload = "key=1b2ea248af8252d4d3ef84d0ef6798ce&txt=" + input_str + "&url=&doc="

    # print payload

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    data = json.loads(response.text)

    language = data['language_list'][0]['name']

    print "Detected language of file " + single_file.name + " is: ", language
