import requests
import json


'''This program detect the language of console 
input from users using MeaningCloud'''

# Input from console
input_str = raw_input("Enter your input: ")

print "Received input: ", input_str

url = "http://api.meaningcloud.com/lang-2.0"

payload = "key=1b2ea248af8252d4d3ef84d0ef6798ce&txt="+input_str+"&url=&doc="

headers = {'content-type': 'application/x-www-form-urlencoded'}


response = requests.request("POST", url, data=payload, headers=headers)

data = json.loads(response.text)

language = data['language_list'][0]['name']

print "Detected language is: ", language