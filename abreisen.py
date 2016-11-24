import mechanize

browser = mechanize.Browser()
browser.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
browser.addheaders = [('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
browser.set_handle_robots(False)

anfrage = mechanize.Request("")


#So koennte man zb abreisen 

branfrage = mechanize.Request("http://de101.die-staemme.de/game.php?village=5512&mode=destroy&screen=main")

browser.open(anfrage)
browser.open(branfrage)
target_url = '/game.php?village=5512&action=downgrade_building&h=03c5&id=hide&screen=main'


for link in browser.links():
    print(link.url)
    if 'hide&screen=main' in link.url:
        print('Gefunden')
        browser.follow_link(link)
        break    
