import os

def clearTerminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

clearTerminal()
class Headphone:
    def __init__(self, brand, name, color, volume, speakers,):
        self.brand = brand
        self.name = name
        self.color = color
        self.volume = volume
        self.speakers = speakers

    def volumeUp(self, volume):
        self.volume += volume
    
    def volumeDown(self, volume):
        self.volume -= volume
    
    def __str__(self):
        return f"Brand: {self.brand} \nType: {self.name}\nColor: {self.color}\nVolume: {self.volume}\nSpeakers: {self.speakers}"

Beats = Headphone("Beats", "Beats Studio Pro", "Blue", 0, 2)
Bose = Headphone("Bose", "Bose QuiteComfort", "Black", 0, 2)
JBL = Headphone("JBL", "JBL On-Ear", "Pink", 0, 2)
Sony = Headphone("Sony", "Sony WH-CH720N", "Maroon", 0, 2)

headPhones = [Beats, Bose, JBL, Sony]
for headphone in headPhones:
    print()
    print(headphone)
    headphone.volumeUp(10)

for headphone in headPhones:
    print()
    headphone.volumeDown(2)
    print(headphone.volume)
