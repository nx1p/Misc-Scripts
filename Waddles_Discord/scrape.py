from urllib.request import urlopen
from lxml import html
import sys

def GetLatestPage():
    page = urlopen("http://archiveofourown.org/tags/Alternate%20Universe%20-%20Transcendence%20(Gravity%20Falls)/works").read().decode('utf-8')
    tree = html.fromstring(page)
    numr = tree.xpath('//*[@id="main"]/ol[1]/li[13]/a')
    number = numr[0].text_content()
    return int(number)

def Process(n):
    print(('Downloading page: ' + n))
    page = urlopen('http://archiveofourown.org/tags/Alternate%20Universe%20-%20Transcendence%20(Gravity%20Falls)/works?page=' + n).read().decode('utf-8')
    print('Parsing')
    tree = html.fromstring(page)
    ids = tree.xpath('//*[@class="work blurb group"]/@id')
    save = open('urls.txt','a')
    for i in ids:
        name = tree.xpath('//*[@id="'+i+'"]/div/h4/a[1]/text()')[0]
        i = i.replace('work_', '')
        save.write('http://archiveofourown.org/works/' + i + ' ' + name+' \n')
        print(('id: ' + i + '    name: ' + name))
    save.close()

def UpdateDatabase():
    save = open('urls.txt','w')
    save.write('')
    save.close()


    for i in range(GetLatestPage()):
        Process(str(i+1))
    print('\nDone')
    print((str(i)))
