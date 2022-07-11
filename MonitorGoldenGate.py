import requests
import json
from SendEmail import *
from base64 import b64encode
from requests.auth import HTTPBasicAuth

#declare array for extracts
aExtracts = []
aReplicats = []
aListAlerts =[]

username = '<username>'
password = '<password>'
url = "<GoldenGate Error>"
encoded_credentials = b64encode(bytes(f'{username}:{password}',
                                encoding='ascii')).decode('ascii') 
auth_header = f'Basic {encoded_credentials}' 
payload=""
header = f'{auth_header}' 
headers = {
  'Authorization':  header,
  'Cookie': ''
}

ListExractsAPI = "/services/v2/extracts"
ListReplicatsAPI = "/services/v2/replicats"

#function to get status of any Extract
def checkStatusExtracts():
    for ext in aExtracts:
        #get status of each extract
        CheckStatusExtract = "/services/v2/extracts/"+ext[0]+"/info/status"
        responseCheckStatus = requests.request("GET", url+CheckStatusExtract, headers=headers, data=payload)
        try:
            status = responseCheckStatus.json()['response']['status']
            if status != 'running':
                #get report from extracts that are not running and save the report
                extractReport = "/services/v2/extracts/"+ext[0]+"/info/reports/"+ext[0]+".rpt"
                responseExtractReport = requests.request("GET", url+extractReport, headers=headers, data=payload)
                ext[1] = responseExtractReport.text
                sendEmail("Error in " + ext[0], ext[0] + " is not running because of " + ext[1] )
                #sendEmail()
            else:
                lag = responseCheckStatus.json()['response']['sinceLagReported']
                print(lag)
                if lag > 10:
                    sendEmail("The Extract  " + ext[0], " has a lag of " + lag )

        except:
            print("error ")
            print(responseCheckStatus.json())
            ext[1] = responseCheckStatus.text
       
#function to get status of any Replicat
def checkStatusReplicats():
    for rep in aReplicats:
        #get status of each Replicat
        CheckStatusReplicat = "/services/v2/replicats/"+rep[0]+"/info/status"
        responseCheckStatus = requests.request("GET", url+CheckStatusReplicat, headers=headers, data=payload)
        try:
            status = responseCheckStatus.json()['response']['status']
            if status != 'running':
                #get report from replicats that are not running and save the report
                extractReport = "/services/v2/replicats/"+rep[0]+"/info/reports/"+rep[0]+".rpt"
                responseReplicatReport = requests.request("GET", url+extractReport, headers=headers, data=payload)
                rep[1] = responseReplicatReport.text
                sendEmail("Error in " + rep[0], rep[0] + " is not running because of " + rep[1] )
            else:
                lag = responseCheckStatus.json()['response']['lag']
                print(responseCheckStatus.json())
                if lag > 10:
                    sendEmail("The Replicat  " + rep[0], " has a lag of " + lag )

        except:
            print(responseCheckStatus.json())
            rep[1] = responseReplicatReport.text

def printMessage(processname, errorType, messageType):
    print("Extract "+ processname  + messageType + errorType)
       

responseListExtracts = requests.request("GET", url+ListExractsAPI, headers=headers, data=payload)
jsonResponse = responseListExtracts.json()['response']['items']
e = json.dumps(jsonResponse)
extractsJson = json.loads(e)

responseListReplicats = requests.request("GET", url+ListReplicatsAPI, headers=headers, data=payload)
jsonResponse = responseListReplicats.json()['response']['items']
r = json.dumps(jsonResponse)
relicatsJson = json.loads(r)

for exts in extractsJson:
    #add extracts name to array
    aExtracts.append([exts['name'],'log error'])

for reps in relicatsJson:
    #add extracts name to array
    aReplicats.append([reps['name'],'log error'])


checkStatusExtracts()
checkStatusReplicats()
