from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
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
SAMPLE_SPREADSHEET_ID = '122JpWqlqbvlni5EodBuNwiXqjzBfAx8aNzBSX35o3h0'




    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
   
    
    
service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="Sheet1!A1:G6").execute()
values = result.get('values', [])
lst = [element for innerList in values for element in innerList]

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

print(Convert(lst))

