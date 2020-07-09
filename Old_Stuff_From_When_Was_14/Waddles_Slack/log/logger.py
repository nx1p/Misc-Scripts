from slackclient import SlackClient
import simplejson as json
import urllib2
import gspread
import time
import datetime
from oauth2client.client import SignedJwtAssertionCredentials
def Userlist():
    url = 'https://slack.com/api/users.list?token=xoxp-8141990049-14705535398-14890407617-81ba12a282&pretty=1'
    raw = urllib2.urlopen(url).read()
    users = json.loads(raw)["members"]
    userlist = {}
    for n in users:
        userlist[n['id']] = n['name']
    return userlist

def ChannelList():
    url = 'https://slack.com/api/channels.list?token=xoxp-8141990049-14705535398-14890407617-81ba12a282&pretty=1'
    raw = urllib2.urlopen(url).read()
    chans = json.loads(raw)["channels"]
    chanlist = {}
    for n in chans:
        chanlist[n['id']] = n['name']
    return chanlist

def GoogleSetup():
    json_key = json.load(open('Waddles-8666b39e1c62.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
    gc = gspread.authorize(credentials)
    print 'Opening Google Docs sheet'
    sh = gc.open("TAU Log")
    return sh

def FindLastLine(wk):
    col = wk.col_values(1)
    for n in range(len(col)):
        if col[n] == '':
            return n+1

#setup
api = 'xoxb-14889967847-ckoZdS4FZJCpx0R3CmunwyXW'
print 'Setting up'
print 'Getting list of Slack users'
users = Userlist()
print 'Getting list of Slack channels'
channels = ChannelList()
print 'Logging into Google Docs'
sheet = GoogleSetup()


#Setup Slack connection
slack = SlackClient(api)

print 'Connecting to Slack'
if slack.rtm_connect():
    print 'Ready'
    while True:
        data = slack.rtm_read()
        if not data == []:
            data = data[0]
            if data['type'] == "message" and "text" in data:
                try:
                    wk = sheet.worksheet(channels[data["channel"]])
                    line = FindLastLine(wk)
                    if not 'username' in data:
                        user = users[data["user"]]
                        msg = data["text"]
                        tmz = datetime.datetime.utcfromtimestamp(float(data["ts"])).strftime('%Y-%m-%d %H:%M:%S')
                        wk.update_cell(line, 1, tmz)
                        wk.update_cell(line, 2, user)
                        wk.update_cell(line, 3, msg)
                        print '[' + tmz + '] ' + user + ': ' + msg
                    elif 'username' in data:
                        user = data["username"]
                        msg = data["text"]
                        tmz = datetime.datetime.utcfromtimestamp(float(data["ts"])).strftime('%Y-%m-%d %H:%M:%S')
                        wk.update_cell(line, 1, tmz)
                        wk.update_cell(line, 2, user)
                        wk.update_cell(line, 3, msg)
                        print '[' + tmz + '] ' + user + ': ' + msg
                except:
                    wk = sheet.worksheet(channels[data["channel"]])
                    wk.update_cell(line, 1, 'Unknown')
                    wk.update_cell(line, 2, 'Waddles')
                    wk.update_cell(line, 3, 'An error has occured, one message has probably been lost')
                    print 'An error has occured'
	time.sleep(1)
