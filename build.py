import mechanize
import linkbuilder
import time

#So koennte man zb abreisen 


def build(village,building,browser):
    
    link = linkbuilder.linkbuilder(village,'build')
    branfrage = mechanize.Request(link)
    browser.open(branfrage)
    
    building += '&screen=main'
    
    for link in browser.links():
        if building in link.url:
            browser.follow_link(link)
            break    

def destroy(village,building,browser):
    link = linkbuilder.linkbuilder(village,'destroy')
    time.sleep(2)
    branfrage = mechanize.Request(link)
    browser.open(branfrage)
    time.sleep(3)
    building += '&screen=main'
    
    for link in browser.links():
        if building in link.url:
            browser.follow_link(link)
            break 