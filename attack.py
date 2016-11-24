import sys
import sqlite3
from mechanize import ParseResponse, urlopen, urljoin
import mechanize
import time
import random
import globals
import linkbuilder
    
def attack(village, spear, sword, axe, spy, light, heavy, ram, catapult, snob, x_cord,y_cord,browser):
    globals.lock.acquire(blocking=1)
    link = linkbuilder.linkbuilder(village,'attack')
    branfrage = mechanize.Request(link)

    response = browser.open(branfrage)
    forms = ParseResponse(response)
    form = forms[0]

    
    control = form.find_control(name = "attack", type="submit")


    
    form["spear"] = spear
    form["sword"] = sword
    form["axe"] = axe
    form["spy"] = spy
    form["light"] = light
    form["heavy"] = heavy
    form["ram"] = ram
    form["catapult"] = catapult
    form["snob"] = snob
    form["x"] = x_cord
    form["y"] = y_cord
    
    oeffnen = form.click(control.name)
    
    antwort = browser.open(oeffnen)
    forms2 = ParseResponse(antwort)
    form2 = forms2[0]

    
    control2 = form2.find_control( type="submit")

    
    oeffnen = form2.click(control2.type)
    browser.open(oeffnen)
    globals.lock.release()
    
def farmb(list,browser):
    conn = sqlite3.connect('tribal.db')
    globals.lock.acquire(blocking=1)
    link = linkbuilder.linkbuilder(1, 'attack')
    tmp = 0
    light = True
    #antwort = mechanize.urlopen(anfrage)
    for i in range(len(list)):
        try:
            #print("Ich bin bei Angriff ",i+1)
            c = conn.cursor()
            c.execute('select x,y from farm where id = (?)', [list[i]])
            coord = [dict(x=row[0], y=row[1]) for row in c.fetchall()]
            xcord = coord[0]['x']
            ycord = coord[0]['y']
            
            
            branfrage = mechanize.Request(link)
            
            
            response = browser.open(branfrage)
            forms = ParseResponse(response)
            form = forms[0]
            #print form
            
            control = form.find_control(name = "attack", type="submit")
            #print control.name, control.value, control.type
            
            
            '''  <TextControl(spear=)>
                  <TextControl(sword=)>
                  <TextControl(axe=)>
                  <TextControl(spy=)>
              <TextControl(light=)>
                  <TextControl(heavy=)>
                  <TextControl(ram=)>
                  <TextControl(catapult=)>
                      <TextControl(snob=)>'''
            
            if light == True:
                form["light"] = "10"
            '''elif axe == True:
                form["axe"] = "10"'''
            form["x"] = str(xcord)
            form["y"] = str(ycord)
            time.sleep(random.uniform(0,1))
            oeffnen = form.click(control.name)
            
            antwort = browser.open(oeffnen)
            forms2 = ParseResponse(antwort)
            form2 = forms2[0]
            #print form2
            
            control2 = form2.find_control(type="submit")
            #print control2.name, control2.value, control2.type
            
            oeffnen2 = form2.click(control2.type)
            browser.open(oeffnen2)
            time.sleep(random.uniform(1,5))
        except:
            if tmp == 0:
                link = linkbuilder.linkbuilder(3,'attack')
                tmp = 1
            elif tmp == 1:
                link = linkbuilder.linkbuilder(4,'attack')
                tmp = 2
            else:    
                i = len(list)+1


        
    
    
    
    conn.close()
    globals.lock.release()
       



    
    




