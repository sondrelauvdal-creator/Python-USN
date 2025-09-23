#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 20:08:34 2025

@author: sondrewistlauvdal

Arbeidskrav 1 

"""

# Import av pakke

import numpy as np

# Kode for beregning av årlig kjørekostnad basert på antall kilometer kjørt årlig

km_inn = input("Skriv inn antall kjørte kilometer per år:")  # Bruker skriver inn kjørelengde

km = float (km_inn)

#Forutsetning for beregning av totalkostnad følger under

# forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.

# trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil

# drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.

# bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

kostnad_bensin = 7500 + (8.38*365) + ((1+0.3)*km )

kostnad_el = 5000 + (8.38*365) + (((0.2*2)+0.1)*km)

diff= kostnad_bensin - kostnad_el

print ( " Bensinbil koster deg årlig " ,kostnad_bensin , " og elbil koster deg årlig ", kostnad_el ,
       " differansen er " , diff)