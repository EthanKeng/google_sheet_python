from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Generate oauth2 credentials
from google.oauth2 import service_account
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1qw233FJtTHnRPrOdywMBfteeuE-eVVyHc92quQjhVKM'
SAMPLE_RANGE_NAME = 'logs!A1:F55'


"""Shows basic usage of the Sheets API.
Prints values from a sample spreadsheet.
"""

try:
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    print(values)
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))
except HttpError as err:
    print(err)
