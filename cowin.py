#!/usr/bin/env python
# coding: utf-8

import requests
import datetime
import json

DIST_ID = 363
age=40
base = datetime.datetime.today()
date_str=base.strftime("%d-%m-%Y")

    #URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(INP_PINCODE, date_str)
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, date_str)
response = requests.get(URL)
if response.ok:
    resp_json = response.json()
    #print(resp_json)
    if resp_json["centers"]:
        for center in resp_json["centers"]:
            for session in center["sessions"]:
                if session["min_age_limit"] <= age:
                    #print(center["name"] + " : " + str(session["available_capacity"]))
                    if (int(session["available_capacity"]) > 0):
                        print(center["name"] + " : pincode : " + str(center["pincode"]) + " : available_capacity : " + str(session["available_capacity"]))
    else:
        print("No available slots on {}".format(INP_DATE))