'''
Only run this program after you have created a Selenium ChromeDriver instance
named browser in the console and logged into bencullivan.com.

The credentials are:
    Username: student
    Password: student
'''
import urllib.request
import os

#open text document containing all saved Test Bank URLs
with open('tb_urls.txt', 'r') as f:
    tb_urls = f.readlines()
    tb_urls = [url.strip() for url in tb_urls]

for url in tb_urls:
    browser.get(url)
    browser.execute_script("GradeIt(document.forms[0])")
    browser.switch_to.alert.accept()
    htmlpath = './TestBanks/{}l'.format('/'.join(url.split('/')[-3:]))
    srcpathbase = '.'.join(htmlpath.split('.')[:-1]) + '_files/'
    with open(htmlpath, 'w') as f:
        f.write(browser.page_source)
        os.mkdir(srcpathbase)
    imgs = browser.find_elements_by_tag_name('img')
    imgurls = [img.get_attribute('src') for img in imgs]
    for imgurl in imgurls:
        srcpath = srcpathbase + imgurl.split('/')[-1]
        urllib.request.urlretrieve(imgurl, srcpath)
    

    
