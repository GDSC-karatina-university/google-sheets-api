from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ELHpu5LiMA_AO6mqITMLQU1VFp4DTTPSxgpman1J-Dg'



service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="fclass!A1:C5").execute()
values = result.get('values', [])
data=[['Fedora', 'F', 20],['Festus','M',17]]
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                            range="fclassUpdate!A1", 
                            valueInputOption="USER_ENTERED", 
                            body={"values":data}).execute()
print(values)

"""
if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))
"""
