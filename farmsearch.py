import sys
import time
import random
from mechanize import ParseResponse, urlopen, urljoin
import mechanize
import sqlite3
import globals






def farmsearch(browser):
    globals.lock.acquire(blocking=1)
    conn = sqlite3.connect('tribal.db')
    c = conn.cursor()
    c.execute("drop table farm")
    conn.commit()
    c.execute("create table farm(id integer primary key, x int, y int)")
    conn.commit
    for i in range(544,562):
        for j in range(486,502):
            try:
                print("ich suche gerade nach",i,"|",j)
                branfrage = mechanize.Request("http://de101.die-staemme.de/game.php?village=5512&screen=place")
                browser.open(branfrage)
    
                response = browser.open(branfrage)
                forms = ParseResponse(response)
                form = forms[0]
                #print form
    
                control = form.find_control(name = "support", type="submit")
                #print control.name, control.value, control.type
    
                form["sword"] = "1"
                form["x"] = str(i)
                form["y"] = str(j)
                oeffnen = form.click(control.name)
                antwort = browser.open(oeffnen)
                forms2 = ParseResponse(antwort)
                form2 = forms2[0]
            
                try:
                    vergleich = form2.find_control(name = "support",type="submit")
                except:
                    player = False
                    for link in browser.links():
                        if "id" in link.url and "info_player" in link.url:
                            player = True
                    if player is False:
                        print i,"|",j
                        c.execute("insert into farm(x,y) values (?,?)",[i,j])
            except Exception, e:
                print e
                print("fehler")
            time.sleep(random.uniform(1, 10))
    print("Fertig mit suchen!")
    conn.commit()
    conn.close()
    globals.lock.release()
    
def randomfarm():
    list = []
    
    for i in range(68):
        list += [0]
        
    for i in range(len(list)):
        loop = True
        while loop is True:
            tmp = random.randint(1,68)
            for j in range(len(list)):
                if tmp == list[j]:
                    break
            else:
                list[i] = tmp
                loop = False
    return list