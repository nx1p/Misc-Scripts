import json
import gspread
import time
from oauth2client.client import SignedJwtAssertionCredentials


print 'Loading creds'
json_key = json.load(open('Waddles-8666b39e1c62.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

print 'Logging in'
gc = gspread.authorize(credentials)
print 'Opening sheet'
sh = gc.open("TAU Log")
wks = sh.sheet1


print 'Running test part'

for i in range(10):
    wks.update_cell(i+1, 1, "test"+str(i+1))
    print 'Done part ' + str(i+1)
