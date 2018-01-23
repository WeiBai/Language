import detectlanguage
import json


'''This program detect the language of console 
input from users using detectlanguae'''

# Input from console
input_str = raw_input("Enter your input: ")

detectlanguage.configuration.api_key = "7750ba3cec7607c4e9a95584b94bb464"
result = detectlanguage.detect(input_str)

print result[0]['language']