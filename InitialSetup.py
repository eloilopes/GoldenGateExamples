import requests
import json
from base64 import b64encode
from requests.auth import HTTPBasicAuth

#declare array for extracts
aExtracts = []
aReplicats = []
aDistributionPath =[]
aListAlerts =[]
replicat=""
distpath=""
version ="v2"
username = '<gg usernamne>'
password = '<password>
sourceUrl = "https://<goldengate hostname>"

listExtractsNames={}
encoded_credentials = b64encode(bytes(f'{username}:{password}',
                                encoding='ascii')).decode('ascii') 
auth_header = f'Basic {encoded_credentials}' 
payload=""
header = f'{auth_header}' 
headers = {
'Authorization':  header,
'Cookie': ''
}

extractAPI = f'/services/{version}/extracts'
replicatAPI = f'/services/{version}/replicats'
distributionPathAPI=f'/services/{version}/sources'

GetExtractCheckPoint = "/services/{version}/extracts/{extract}/info/checkpoints"
GetReplicatCheckPoint = "/services/{version}/replicats/{replicat}/info/checkpoints"
retrieveReplicat =f'/services/{version}/replicats/' 
retrieveExtract =f'/services/{version}/extracts/' 


#Example for GoldenGate Initial Load.
bodyInitialLoad = {
            'config': ["Extract IL2","ExtFile a5 Megabytes 2000 Purge","UseridAlias ADW DOMAIN OracleGoldenGate","Table ODI_DEMO.TRG_COUNTRY;"],
            'source': 'tables'
        }

#Example for GoldenGate Integrated Extract.
bodyExtract = {
            'config': ["Extract ext4","ExtTrail a1","UseridAlias ADW DOMAIN OracleGoldenGate","Table ODI_DEMO.TRG_COUNTRY;"],
            'source': 'tranlogs',
            'credentials': {"alias":"ADW","domain":"OracleGoldenGate"},
            'begin': 'now',
            'targets': [
                {
                    'name': 'a1',
                    'sizeMB': 500
                }
            ]
        }

#Example for GoldenGate Integrated Parallel replicat.
bodyReplicatIntegratedParallel = {
            'config': ["Replicat Rep4","UseridAlias SQLServerConnection DOMAIN OracleGoldenGate","Map ODI_DEMO.TRG_COUNTRY,","Target dbo.COUNTRY;"],
            'source': {
                'name': 'a1'
            },
            'credentials': {"alias":"SQLServerConnection","domain":"OracleGoldenGate"},
            'checkpoint':{
                'table': 'dbo.checkpoint_table'#jsonResponseRetrieveReplicat['checkpoint']
             },
            'mode': {
                'type': 'integrated', 
                'parallel': True
                }
        }

#Example for GoldenGate Integrated replicat.
bodyReplicatIntegrated = {
            'config': ["Replicat Rep5","UseridAlias SQLServerConnection DOMAIN OracleGoldenGate","Map ODI_DEMO.TRG_COUNTRY,","Target dbo.COUNTRY;"],
            'source': {
                'name': 'a1'
            },
            'credentials': {"alias":"SQLServerConnection","domain":"OracleGoldenGate"},
            'checkpoint':{
                'table': 'dbo.checkpoint_table'
             },
            'mode': {
                'type': 'integrated', 
                'parallel': False
                }
        }

#Example for GoldenGate Non Integrated replicat.
bodyReplicatNonIntegrated = {
            'config': ["Replicat Rep6","USERIDALIAS ADW DOMAIN OracleGoldenGate","Map ODI_DEMO.TRG_COUNTRY,","Target ODI_DEMO.TRG_COUNTRY;"],
            'source': {
                'name': 'a1'
            },
            'credentials': {"alias":"ADW","domain":"OracleGoldenGate"},
            'checkpoint':{
                'table': 'ODI_DEMO.ADW_CHECKTABLE'
             },
            'mode': {
                'type': 'nonintegrated', 
                'parallel': False
                }
        }

#Example for GoldenGate Non Integrated Parallel replicat.
bodyReplicatNonIntegratedParallel = {
            'config': ["Replicat Rep7","USERIDALIAS ADW DOMAIN OracleGoldenGate","Map ODI_DEMO.TRG_COUNTRY,","Target ODI_DEMO.TRG_COUNTRY;"],
            'source': {
                'name': 'a1'
            },
            'credentials': {"alias":"ADW","domain":"OracleGoldenGate"},
            'checkpoint':{
                'table': 'ODI_DEMO.ADW_CHECKTABLE'
             },
            'mode': {
                'type': 'nonintegrated', 
                'parallel': True
                }
        }

#Example for GoldenGate Coordinated replicat.
bodyReplicatCoordinated = {
            'config': ["Replicat Rep8","USERIDALIAS ADW DOMAIN OracleGoldenGate","Map ODI_DEMO.TRG_COUNTRY,","Target ODI_DEMO.TRG_COUNTRY;"],
            'source': {
                'name': 'a1'
            },
            'credentials': {"alias":"ADW","domain":"OracleGoldenGate"},
            'checkpoint':{
                'table': 'ODI_DEMO.ADW_CHECKTABLE'
             },
            'mode': {
                'type': 'coordinated',
                'maxThreads': 10
                }
        }




def createExtract(inputExtract, inputHearders, inputBody,url):
    responsePost = requests.post(url+extractAPI+'/'+inputExtract, headers=inputHearders, json=inputBody)
    print (responsePost.json())

def createReplicat(inputReplicat, inputHearders, inputBody, url):
    responsePost = requests.post(url+replicatAPI+'/'+inputReplicat, headers=inputHearders, json=inputBody)
    print (responsePost.json())

def startExtract(inputExtract,inputHearders, url):
    inputBody = {"status":"running"}
    responsePost = requests.patch(url+extractAPI+'/'+inputExtract, headers=inputHearders, json=inputBody)
    print (responsePost.json())

def stopExtract(inputExtract,url):
    inputBody = {"status":"stopped"}
    responsePost = requests.patch(url+extractAPI+'/'+inputExtract, headers=headers, json=inputBody)
    print (responsePost.json())

def deleteExtract(inputExtract,url):
    responsePost = requests.delete(url+extractAPI+'/'+inputExtract, headers=headers, json=payload)
    print (responsePost.json())

def startReplicat(inputReplicat,inputHearders,url):
    inputBody = {"status":"running"}
    responsePost = requests.patch(url+replicatAPI+'/'+inputReplicat, headers=inputHearders, json=inputBody)
    print (responsePost.json())

def stopReplicat(inputReplicat,inputHearders,url):
    inputBody = {"status":"stopped"}
    responsePost = requests.patch(url+replicatAPI+'/'+inputReplicat, headers=inputHearders, json=inputBody)
    print (responsePost.json())

def deleteReplicat(inputReplicat,url):
    responsePost = requests.patch(url+replicatAPI+'/'+inputReplicat, headers=headers, json=payload)
    print (responsePost.json())


#createExtract('EXT4', headers,bodyExtract,sourceUrl)

#createReplicat('REP8',headers,bodyReplicatCoordinated,sourceUrl)

#for initial load
#createExtract('IL2', headers, bodyInitialLoad,sourceUrl)
