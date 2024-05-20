from machine import Pin, SPI
import ili9342c
import axp202c
import random as rand

class Rechteck(): # Klasse erstellen
    def __init__(self, pos_x, pos_y, breite, hoehe, objekt): # Parameter erstellen
        # abspeichern der information 
        self.pos_x = pos_x 
        self.pos_y = pos_y
        self.breite = breite
        self.hoehe = hoehe
        self.objekt = objekt

    def draw(self): # draw methoden zum ausfuellen
        self.objekt.fill_rect(self.pos_x, self.pos_y, self.breite + 6, self.hoehe + 6, color=ili9342c.BLACK)
        self.objekt.fill_rect(self.pos_x+3, self.pos_y+3, self.breite, self.hoehe, color=rand.randint(0, 65535))


def main():
    axp = axp202c.PMU(address=0x34)  # PMU einbinden
    axp.enablePower(axp202c.AXP192_LDO2)  # Display anschalten
    axp.setDC3Voltage(3000)  # Hintergrundbeleuchtung einstellen
    spi = SPI(2, baudrate=60000000, sck=Pin(18), mosi=Pin(23))  # SPI init
    tft = ili9342c.ILI9342C(spi, 320, 240, cs=Pin(5, Pin.OUT),
    dc=Pin(15, Pin.OUT), rotation=0)  # Display init

    tft.clear(ili9342c.WHITE) #Hintergrund auf Weiß setzen
    zeile = 5 # n fuer Zeilen
    spalte = 5 # m fuer Spalten
    anzahl_zeile = 320 // zeile # anzahl der in Displaybreite passenden Objekte
    anzahl_spalte = 240 // spalte # anzahl der in Displayhohe passenden Objekte

    rechteck = [] # liste zum abspeichern
    for x in range(zeile): # zeilen durchlauf
        for y in range(spalte): # splaten durchlauf
            # rechteck in die liste hinzufuegen
            rechteck.append(Rechteck(x * anzahl_zeile, y * anzahl_spalte, anzahl_zeile - 13, anzahl_spalte - 13, tft))

    for i in rechteck: # geht jedes element in der liste durch
        i.draw() # fuhert fuer jedes element die methode aus

if __name__ == "__main__":
    main()
