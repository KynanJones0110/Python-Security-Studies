import requests
import json
import pandas
import csv
import sys

#If you're using office online you can only export as excel docs as .xlsx, I'd suggest just using Google sheets :)

file_path = str(input("File Path: "))
IP_CSV = pandas.read_csv((file_path))

ip=IP_CSV["IP"].tolist()

#You will need to create a free account for this
API_KEY = "ENTER API KEY"
url = 'https://api.abuseipdb.com/api/v2/check'
validate_key = len(API_KEY)
csv_columns = ['ipAddress','isPublic','ipVersion','isWhitelisted','abuseConfidenceScore','countryCode','usageType','isp','domain','hostnames','totalReports','numDistinctUsers','lastReportedAt']

headers = {
    'Accept': 'application/json',
    'Key': API_KEY
}
# check key 
if validate_key < 13: #change for better handling sometime
    print("You need to enter your API key, the variable name is 'API_KEY'")
    sys.exit()
else:
    print("API key is valid. Continuing with the program...")


with open("AbuseIP_results.csv","a", newline='') as filecsv:
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    writer.writeheader()
for i in ip:
    parameters = {
        'ipAddress': i,
        'maxAgeInDays': '90'}

    response= requests.get( url=url,headers=headers,params=parameters)
    json_Data = json.loads(response.content)
    json_main = json_Data["data"]
    with open("AbuseIP_results.csv","a", newline='')as filecsv:
        writer= csv.DictWriter(filecsv,fieldnames=csv_columns)
        writer.writerow(json_main)
        
#Offical Documentation on Bulk Reporting: https://docs.abuseipdb.com/#bulk-report-endpoint and https://www.abuseipdb.com/bulk-report
