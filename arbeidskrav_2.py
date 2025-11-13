#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 09:50:08 2025

@author: sondrewistlauvdal

Arbeidskrav 2 til innlevering PY 1010. 

Samtlige oppgaver/scripts/programmer lagret i samme fil for enklere levering i Canvas.

Relevante pakker for forskjellige oppgaver importert i starten scriptet. 

"""

import numpy as np
import matplotlib.pyplot as plt


"Oppgave 1"
#Du skal her lage et program som skal starter med
#alder = int(input('Hvilket år er du født? ') )
#Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive
#svaret til skjerm med passende tekst.

alder = int(input('Hvilket år er du født? ') ) #Bruker skriver inn alder
alder_2024=2024-alder
print(" I år 2024 fyller du:", alder_2024, "år")


"Oppgave 2"
#Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et
#program som tar inn antall elever fra konsollen ved
#antall_elever = int(input('Skriv inn antall elever:' ))
#Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive
#svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe
#5).
#Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
#Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan
#sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?

antall_elever = int(input('Skriv inn antall elever som skal ha pizza på fest:' )) #Bruker skriver inn antall elever
antall_pizzaer = antall_elever/4
antall_pizzaer_rundetopp = np.ceil(antall_pizzaer) #Runder opp til hele pizzaer
print("Det må kjøpes inn", antall_pizzaer_rundetopp, "pizzaer")


"Oppgave 3"
#Lag et program med en funksjon som regner om fra grader til radianer.
#Programmet skal starte med:
#v_grad = float(input('Skriv inn gradtallet:' ))
#Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
#Resultatet v_rad skrives til skjerm med passende tekst og verdi.
#Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....


v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180 #Omskriver fra grader til radianer
v_rad_avrundet = round(v_rad, 2) # Begrenser til 2 desimaler i svaret
broek_foran_pi = v_grad/180


print(v_grad, "grader svarer til", v_rad_avrundet, "radianer, tilsvarende", broek_foran_pi, "pi")


"Oppgave 4"

"4a"
#Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
#og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.

data={"Norge":["Oslo", 0.643], "England": ["London", 8.982], "Frankrike": ["Paris", 2.161]
         , "Italia": ["Roma", 2.873]}

"4b"
#Lag et program som ber brukeren skrive inn et land (eksempelvis England).
#Programmet skal på bakgrunn av dette skrive ut følgende setning:
#London er hovedstaden i England og det er 8.982 mill. innbyggere i London

land=input('Skriv inn ett av følgende land: Norge, England, Frankrike eller Italia: ' )

print(data[land][0], "er hovedstaden i", land,  "og det er", data[land][1], "millioner innbyggere i " , data[land][0] )


"4c"
#lag et program som ber brukeren skrive inn info om et nytt land (altså et land som
#ikke allerede finnes i dictionaryen data). Videre skal brukeren oppgi hovedstad og
#antall innbyggere for det «nye» landet. Programmet skal så utvide/oppdatere
#dictionaryen med den nye informasjonen. Dictionaryen data skrives så til skjerm.

nytt_land=input("skriv inn et land:")
hovedstad=input("skriv inn hovedstad i landet")
innbyggere=float(input("skriv inn antall millioner innbyggere i landet"))
data[nytt_land] = [hovedstad, innbyggere] #Opprettes ny nøkkel med verdier for hovedstad og innbyggere i dictionary


print(data)

"Oppgave 5"

#Lag et program med en funksjon som tar a og b som inn-argumenter og som så
#regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
#halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
#Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
#tekst.



a=float(input("angi korteste katet a i en trekant")) #ene katet
b=float(input("angi lengste katet b i en trekant")) # andre katet

areal_trekant = 0.5 * a * b
areal_halvsirkel = 0.5 * np.pi * (a / 2)**2
totalt_areal=areal_halvsirkel+areal_trekant #areal for illustrasjonen er summen av figurene
totalt_arealt_avrundet=round(totalt_areal, 2)

omkrets = b + (np.sqrt(a**2 + b**2)) + 0.5 * np.pi * a #Omkrets for angitte figur, ene katet utelatt
omkrets_avrundet=round(omkrets, 2)


print("areal av figuren er", totalt_arealt_avrundet , "ytre omkrets er", omkrets_avrundet)

"Oppgave 6"
#Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10].
#Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
#[-10,10].


x=np.linspace(-10, 10, 200)
f=-2**x-5
                 
plt.close('all') # lukker alle åpne vinduer for å spare plass
plt.figure(1) # angir at dette er hovedplottet i figuren, kan legges på flere
plt.plot(x, f, 'g*-', label='funksjon') 


