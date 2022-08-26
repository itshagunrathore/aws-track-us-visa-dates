import json

import boto3
import requests

from datetime import date

today = date.today()
print("Today's date:", today)
with open('data.json') as f:
    mymap = json.load(f)
    f.close()
print(mymap)

flag = False
client = boto3.client("sns",
                      aws_access_key_id="<>",
                      aws_secret_access_key="<>"
                      , region_name="ap-south-1")


response = requests.get(
    "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P139&aid=VisaWaitTimesHomePage")
r = response.text.strip().split()[0]

print("MUMBAI " + r)
if (int(mymap.get("M")) != int(r)):
    flag = True
    mymap["M"] = int(r)

response = requests.get(
    "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P48&aid=VisaWaitTimesHomePage")
r = response.text.strip().split()[0]

print("CHENNAI " + r)
if int(mymap.get("C")) != int(r):
    flag = True
    mymap["C"] = int(r)

response = requests.get(
    "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P100&aid=VisaWaitTimesHomePage")
r = response.text.strip().split()[0]

print("KOLKATA " + r)
if int(mymap.get("K")) != int(r):
    flag = True
    mymap["K"] = int(r)


response = requests.get(
    "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P147&aid=VisaWaitTimesHomePage")
r = response.text.strip().split()[0]
print("DEHLI " + r)
if int(mymap.get("D")) != int(r):
    flag = True
    mymap["D"] = int(r)

response = requests.get(
    "https://travel.state.gov/content/travel/resources/database/database.getVisaWaitTimes.html?cid=P85&aid=VisaWaitTimesHomePage")
r = response.text.strip().split()[0]
print("Hyderabad " + r)
if int(mymap.get("H")) != int(r):
    flag = True
    mymap["H"] = int(r)

w_file = open('data.json', "w")
json.dump(mymap, w_file)
w_file.close()

if flag is True:
    print("Sending Text MSG")
    client.publish(TopicArn="arn:aws:sns:ap-south-1:044601433012:shagunvisatopic", Message=f"Visa wait times has changed: {json.dumps(mymap)}", MessageStructure="None")
