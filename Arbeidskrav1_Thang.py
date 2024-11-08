# -*- coding: utf-8 -*-
"""
Arbeidskrav 1
Sammenlikning årlige kostnader mellom bensinbil og elbil, 10 000km kjørelengde
"""

K = 10000       #Årlig kjørelengde km
T = 8.38*365    #Trafikkforsikringsavgift 
FE = 5000       #Forsikring elbil årlig
FB = 7500       #Forsikring bensinbil årlig
SP = 2          #Strømpris kr/kWh
S = 0.2*SP*K    #Strømforbruk elbil, 0,2 er forbruket pr km i kWh 
B = 1           #Bensinpris kr/km
BF = K*B        #Bensinforbuk 
BE = 0.1*K      #Bomavgift elbil 0,1kr/km
BB = 0.3*K


"""
Totale kostnader elbil
"""

TE=FE+T+S+BE #Total kostnader for elbil
print ('Total kostnad elbil årlig er', TE , 'kr')

"""
Totale kostnader bensinbil
"""

TB=FB+T+BF+BB
print ('Total kostnad bensinbil årlig er', TB , 'kr')


D=TB-TE #Differansen mellom bensinbil og elbil

print ('Man sparer', D , 'kr pr år ved å velge elbil framfor bensinbil')