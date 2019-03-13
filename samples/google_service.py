from apiclient import discovery
from google.auth.transport.urllib3 import AuthorizedHttp

def change_owner(spreadsheet_id, owner):
    '''
    Use the drive api to change the owner
    '''
    drive_service = discovery.build('drive', 'v3')

    permission = drive_service.permissions().create(
        fileId=spreadsheet_id,
        transferOwnership=True,
        body={
            'type': 'user',
            'role': 'owner',
            'emailAddress': owner,
        }
    ).execute()

    drive_service.files().update(
        fileId=spreadsheet_id,
        body={'permissionIds': [permission['id']]}
    ).execute()

def create(title='NoTitle', data=[], owner=None):
    '''
    Use the sheets API to create a sheet
    '''
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', discoveryServiceUrl=discoveryUrl)

    body = dict(properties=dict(title=title))
    spreadsheet = service.spreadsheets().create(body=body).execute()
    spreadsheet_id = spreadsheet['spreadsheetId']

    # 96 is the ascii value of the character before 'a'
    last_column = 96 + len(data[0])
    col = str(chr(last_column))
    rows = len(data)
    update_body = dict(values=data)
    sheet_range = 'a1:{}{}'.format(col, rows)

    service.spreadsheets().values() \
                          .update(spreadsheetId=spreadsheet_id,
                                  valueInputOption='RAW',
                                  range=sheet_range,
                                  body=update_body) \
                          .execute()

    change_owner(spreadsheet_id, owner)

data = []
for i in range(4):
    data.append([4, 3, 2])
create("Test Doc", data, owner="thiswontwork@mailinator.com")
