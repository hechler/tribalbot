import attack
import farmsearch
import support
import sqlite3
import time
from datetime import datetime
from datetime import timedelta
import sys
from mechanize import ParseResponse, urlopen, urljoin
import mechanize
import threading
import globals
import build

#Baut die allgemeine verbindung zu die staemme auf. Fordert quasi einen cockie an. Dieser kann dann spaeter weiterverwendet werden
def connection():
    browser = mechanize.Browser()
    browser.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
    browser.addheaders = [('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
    browser.set_handle_robots(False)
    
    
    anfrage = mechanize.Request("")
    browser.open(anfrage) 
    return browser

def attackmanuel():
    attacks = []
    if len(sys.argv) is 2 or len(sys.argv) is 1:
        tmp = raw_input("Wann willst du starten? Y-M-D-H-M-S: ")
        village = raw_input("Herkunftsdorf?: ")
        weiter = True
        while True:
            
            spear = raw_input("Wie viele Speere?: ")
            sword = raw_input("Wie viele Schwerter?: ")
            axe = raw_input("Wie viele Aexte?: ")
            spy = raw_input("Wie viele Spione?: ")
            light = raw_input("Wie viele Leichte Kav?: ")
            heavy = raw_input("Wie viele Schwere Kav?: ")
            ram = raw_input("Wie viele Rammen?: ")
            catapult = raw_input("Wie viele Katapulte?: ")
            snob = raw_input("Wie viele AG's?: ")
            x_cord = raw_input("X: ")
            y_cord = raw_input("Y: ")
            question = raw_input("Noch einen angriff? 1:Ja 2:Nein :")
            attacks += [dict(village=village,spear=spear, sword=sword, axe=axe, spy=spy, light=light, heavy=heavy, ram=ram, catapult=catapult, snob=snob, x_cord=x_cord, y_cord = y_cord )]
            if question == "2":
                break
            
        now = datetime.now()
        start_at = datetime.strptime(tmp, "%Y-%m-%d-%H-%M-%S") - now
            
    else:
        now = datetime.now()
        start_at = datetime.strptime(sys.argv[2], "%Y-%m-%d-%H-%M-%S") - now

    
    globals.lock_main.release()
    time.sleep(start_at.total_seconds())
    if len(sys.argv) is 2 or len(sys.argv) is 1:
        #globals.lock.acquire(blocking=1)
        browser = connection()
        for i in range(len(attacks)):
            thread = threading.Thread(target=attack.attack, args=(attacks[i]['village'],attacks[i]['spear'],attacks[i]['sword'],attacks[i]['axe'],attacks[i]['spy'],attacks[i]['light'],attacks[i]['heavy'],attacks[i]['ram'],attacks[i]['catapult'],attacks[i]['snob'],attacks[i]['x_cord'],attacks[i]['y_cord'],browser))
            globals.my_threads.append(thread)
            thread.start()
        
    else:
        try:
            browser
        except UnboundLocalError:
            browser = connection()
        else:
            pass
        attack.attack(sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13],sys.argv[3],sys.argv[4],browser)

def building(action):
    village = raw_input("Wich village? >")
    print("main    barracks    stable    garage")
    print("snob    smith       place     market")
    print("wood    stone       iron      farm")
    print("storage hide        wall")
    building = raw_input("Wich building?: > ")
    tmp = raw_input("When to start? Y-M-D-H-M-S: >")
    globals.lock_main.release()
    now = datetime.now()
    start_at = datetime.strptime(tmp, "%Y-%m-%d-%H-%M-%S") - now
    time.sleep(start_at.total_seconds())
    browser = connection()
    if action is 1:
        thread = threading.Thread(target=build.build, args=(village,building,browser))
        globals.my_threads.append(thread)
        thread.start()
    else:
        thread = threading.Thread(target=build.destroy, args=(village,building,browser))
        globals.my_threads.append(thread)
        thread.start()


def main():    
    if len(sys.argv) is 1:
        while True:
            print("Was ist zu tun?")
            print("1: Farm        2: New farm list")
            print("3: Attack      4: Build")
            print("5: Destroy     6: Quit")
            task = raw_input("Aufgabe eineben: ")
            
            if task == '1':
                list = farmsearch.randomfarm()
                browser = connection()
                thread = threading.Thread(target=attack.farmb, args=(list,browser))
                globals.my_threads.append(thread)
                thread.start()
            
            if task == '2':
                thread = threading.Thread(target=farmsearch.farmsearch, args=(connection(),))
                globals.my_threads.append(thread)
                thread.start()
            
            if task == '3':
                globals.lock_main.acquire()
                thread = threading.Thread(target=attackmanuel)
                globals.my_threads.append(thread)
                thread.start()
                while globals.lock_main.locked() is True:
                    time.sleep(10)
            if task == '4':
                globals.lock_main.acquire()
                thread = threading.Thread(target=building, args=(1,))
                globals.my_threads.append(thread)
                thread.start()
                while globals.lock_main.locked() is True:
                    time.sleep(10)
            if task == '5':
                globals.lock_main.acquire()
                thread = threading.Thread(target=building, args=(2,))
                globals.my_threads.append(thread)
                thread.start()
                while globals.lock_main.locked() is True:
                    time.sleep(10)
            if task == '6':
                for t in globals.my_threads:
                    t.join()
                    sys.exit()
                sys.exit()
    
    else:
        if 'attack' in sys.argv:
            attackmanuel()
       
        if 'farm' in sys.argv:
            browser = connection()
            list = farmsearch.randomfarm()
            attack.farmb(list, browser)

        if 'night' in sys.argv:
            for i in range(21):
                browser = connection()
                list = farmsearch.randomfarm()
                attack.farmb(list,browser)
                if i is 20:
                    sys.exit()
                #Waiting for two hours
                now = datetime.now()
                start = now.replace(hour = now.minutes+30)
                start = (start - now).total_seconds()
                time.sleep(start)
                
                
if __name__ == "__main__":
    main()  

