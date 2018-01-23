import requests
import json
import os

'''This program detects the language of the content of a text file'''
# read from a file
file_input = open("news.txt", "r+")

input_str = file_input.read(50);

url = "http://api.meaningcloud.com/lang-2.0"

payload = "key=1b2ea248af8252d4d3ef84d0ef6798ce&txt="+input_str+"&url=&doc="

#print payload

headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

data = json.loads(response.text)

language = data['language_list'][0]['name']

print "Detected language of file " + file_input.name+ " is: ", language
