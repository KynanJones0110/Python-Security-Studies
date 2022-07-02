import requests
import json
import pandas
import csv

#If you're using office online you can only export as excel docs as .xlsx, I'd suggest just using Google sheets :)

file_path = str(input("File Path: "))
IP_CSV = pandas.read_csv((file_path))

ip=IP_CSV["IP"].tolist()

#You will need to create a free account for this
API_KEY = "ENTER YOUR API"
url = 'https://api.abuseipdb.com/api/v2/check'

csv_columns = ['ipAddress','isPublic','ipVersion','isWhitelisted','abuseConfidenceScore','countryCode','usageType','isp','domain','hostnames','totalReports','numDistinctUsers','lastReportedAt']

headers = {
    'Accept': 'application/json',
    'Key': API_KEY
}
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
