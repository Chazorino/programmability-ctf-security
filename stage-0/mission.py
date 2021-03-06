#!/usr/bin/env python

import requests
import json
import sys
from pathlib import Path
import webexteamssdk
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

here = Path(__file__).parent.absolute()
repository_root = (here / ".." ).resolve()
sys.path.insert(0, str(repository_root))

import env

inv_host = env.UMBRELLA.get("inv_url")
api_key = env.UMBRELLA.get("inv_token")
#Use a domain of your choice
domain = "yourdomain.example"

#Construct the API request to the Umbrella Investigate API to query for the status of the domain
url = 
headers = 
response = 
#And don't forget to check for errors during the call!


domain_status = response.json()[domain]["status"]

if domain_status == 1:
    print(f"The domain {domain} is found CLEAN")
elif domain_status == -1:
    print(f"The domain {domain} is found MALICIOUS")
    umbrella_malicious_domains.append(domain)
elif domain_status == 0:
    print(f"The domain {domain} is found UNDEFINED")

print("This is how the response from Umbrella Investigate looks like: \n" + pprint(response.json(), indent=4)