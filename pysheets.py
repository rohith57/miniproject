from __future__ import print_function

import os.path
import google.auth.transport.requests
import requests

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = None


creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)



# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1RHLjYx5pj64ikRjL5tLguq8fplG54Wrulz6e_tvhcaw'




    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
   
    
    
service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
sheet = service.spreadsheets()
#result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                   # range="Sheet1!A1:C6").execute()
#values = result.get('values', [])
#lst = [element for innerList in values for element in innerList]

#def Convert(lst):
    #res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    #return res_dct

#print(Convert(lst))

result =  sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Sheet1!A1:B6").execute()
values = result.get('values',[])
lst = [element for innerlist in values for element in innerlist]
def rackA(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    print(res_dct) 
result1 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Sheet1!C1:D6").execute()

values1 = result1.get('values',[])
lst1 = [element for innerlist in values1 for element in innerlist]
def rackB(lst1):
    res_dect1 = {lst1[i]: lst1[i+1] for i in range(0, len(lst1),2)}
    print(res_dect1)


result2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Sheet1!E1:F6").execute()

values2 = result2.get('values',[])
lst2 = [element for innerlist in values2 for element in innerlist]
def rackC(lst2):
    res_dect2 = {lst2[i]: lst2[i+1] for i in range(0, len(lst2),2)}
    print(res_dect2)

rackA(lst)





