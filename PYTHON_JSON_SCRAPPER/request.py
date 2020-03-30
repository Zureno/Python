#!/usr/bin/env python

import json
import pprint 
import requests
from optparse import OptionParser
import sys
import re

def usage():
	
	print ("""
					 ───▄████▄─────
				 	 ──███▄█▀──────
					 ─▐████──█──█──
					 ──█████▄──────
					 ───▀████▀─────""")
	print ("               -----------------------------------------------------------------")
	print ("                SCRAPPY SCRAPPER :- A SIMPLE PYTHON BASED URL JSON SCRAPPER.")
	print ("               -----------------------------------------------------------------")
	print ("                              SPECIAL CREDITS  :- NUALA GAFFEY")
	print ("                 ************************************************************")
	print ("                                                                                ")

def filtering(git_url):
	
	response = requests.get(git_url)
	json_data = response.json()
	#print(json.dumps(json_data, indent=4, sort_keys=True)) ## printing out the file in json format.
	u_name = json.dumps(json_data["auth_username"])
	print ("Name:-",u_name)
	u_team = json.dumps(json_data["team"])
	print ("Team:-",u_team)

def operator():

        git_url = ""
        parser = OptionParser()
        parser.add_option('-u','--url', dest = 'git_url', type ='string',help = 'Specify a  datafeed url of etsy')
        (options,args) = parser.parse_args()
        git_url = options.git_url
        if git_url == None:
                print (parser.usage)
                exit(0)
        else:
                filtering(git_url)

def main():
      usage()
      operator()
             
if __name__=='__main__':
        main()

