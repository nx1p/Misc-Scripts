import requests
from lxml import html

def Process(n):
    print 'Downloading page: ' + n
    page = requests.get('http://archiveofourown.org/tags/Alternate%20Universe%20-%20Transcendence/works?page=' + n)
    print 'Parsing'
    tree = html.fromstring(page.content)
    ids = tree.xpath('//*[@class="work blurb group"]/@id')
    sumer = tree.xpath('//*[@class="userstuff summary"]')
    save = open('urls.txt','a')
    savesumer = open('summary.txt','a')
    for i in ids:
        name = tree.xpath('//*[@id="'+i+'"]/div/h4/a[1]/text()')[0]
        i = i.replace('work_', '')
        save.write('http://archiveofourown.org/works/' + i + ' ' + name.encode('utf-8')+' \n')
        print 'id: ' + i + '    name: ' + name.encode('utf-8')
    save.close()
    for i in sumer:
        i = i.text_content()
        savesumer.write(i.encode('utf-8') + '|||')
    savesumer.close()

Process('1')
Process('2')
Process('3')
Process('4')
Process('5')
Process('6')
Process('7')
Process('8')
Process('9')
Process('10')
Process('11')
Process('12')
Process('13')
Process('14')
Process('15')
print 'Done'
