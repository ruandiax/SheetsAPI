import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '###'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="page!a1:g30").execute()


values = result.get('values', [])

firstEntry = [[6300, 5355, 4016.25, 1338.75, 945, "Example 1"]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="page!A2",
                                valueInputOption="USER_ENTERED", body={"values": firstEntry}).execute()
