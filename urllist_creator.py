
'''
These were separate throwaway scripts that I kept in a document, they helped 
create the list of urls for each test bank (I was not about to manually do that)

So some variables in this aren't actually defined but they were in the
workspace at the time of writing this, not an important part of the project

Went towards tb_urls.txt
'''


microurls = ["http://bencullivan.com/New/ap-economics/micro-unit-{0}/micro-{0}-test-resources.html".format(i) for i in range(1,7)]
macrourls = ["http://bencullivan.com/New/ap-economics/macro-unit-{0}/macro-{0}-test-resources.html".format(i) for i in range(2,6)]
with open('tr_urls.txt', 'w') as f:
    f.writelines(url + '\n' for url in microurls)
    f.writelines(url + '\n' for url in macrourls)
    
###############################################################################

from lxml import html
for url in urls:
    key = url.split('/')[5]
    browser.get(url)
    doc = html.fromstring(browser.page_source)
    test_banks = doc.xpath('//a[contains(text(), "Test Bank")]/@href')
    bank_urls[key] = test_banks





