import sys
from mechanize import ParseResponse, urlopen, urljoin
import mechanize


def support(x_cord, y_cord, browser):
    
    branfrage = mechanize.Request("http://de101.die-staemme.de/game.php?village=5512&screen=place")
   

    
    response = browser.open(branfrage)
    forms = ParseResponse(response)
    form = forms[0]
    #print form
    
    control = form.find_control(name = "support", type="submit")
    #print control.name, control.value, control.type
    
    
    
    
    form["sword"] = "180"
    form["x"] = str(x_cord)
    form["y"] = str(y_cord)
    
    oeffnen = form.click(control.name)
    
    antwort = browser.open(oeffnen)
    forms2 = ParseResponse(antwort)
    form2 = forms2[0]
    #print form2
    
    control2 = form2.find_control( type="submit")
    #print control2.name, control2.value, control2.type
    
    oeffnen = form2.click(control2.type)
    browser.open(oeffnen)












