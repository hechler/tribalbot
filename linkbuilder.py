import sqlite3



def linkbuilder(village, action):
    conn = sqlite3.connect('tribal.db')
    c = conn.cursor()
    c.execute("select id from ownvillages where bezeichnung = (?)", (village,))
    villageid = [dict(id=row[0]) for row in c.fetchall()]
    conn.close()
    if action is 'build':
        link = 'http://de101.die-staemme.de/game.php?village=****&screen=main'
        link = link.replace('****', str(villageid[0]['id']))
        return link
    if action is 'destroy':
        link = 'http://de101.die-staemme.de/game.php?village=****&screen=main&mode=destroy'
        link = link.replace('****', str(villageid[0]['id']))
        return link
    if action is 'attack':
        link = 'http://de101.die-staemme.de/game.php?village=****&screen=place'
        link = link.replace('****', str(villageid[0]['id']))
        return link

