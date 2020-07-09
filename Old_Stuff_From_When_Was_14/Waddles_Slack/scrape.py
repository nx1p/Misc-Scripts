import requests
from lxml import html
import sys

def Process(n):
    print 'Downloading page: ' + n
    page = requests.get('http://archiveofourown.org/tags/Alternate%20Universe%20-%20Transcendence%20(Gravity%20Falls)/works?page=' + n)
    print 'Parsing'
    tree = html.fromstring(page.content)
    ids = tree.xpath('//*[@class="work blurb group"]/@id')
    save = open('urls.txt','a')
    for i in ids:
        name = tree.xpath('//*[@id="'+i+'"]/div/h4/a[1]/text()')[0]
        i = i.replace('work_', '')
        save.write('http://archiveofourown.org/works/' + i + ' ' + name.encode('utf-8')+' \n')
        print 'id: ' + i + '    name: ' + name.encode('utf-8')
    save.close()
save = open('urls.txt','w')
save.write('')
save.close()


for i in range(int(sys.argv[1])):
    Process(str(i+1))
print '\nDone'
