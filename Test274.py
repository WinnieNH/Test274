import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


urlpoke = "https://pokeapi.co/api/v2/pokemon?limit=721&offset=0"
response = requests.get(urlpoke)
jsonp = response.json()

datacol = json.loads(response.text)

df = pd.DataFrame(jsonp) #gebruikt om om te zetten naar csv

df.to_csv("PokeOutput.csv", encoding="utf-8", index=False)

collectivebase = [] #array voor berekenen base exp maplotlib functie

minweight = 1 #min en max weight opgezocht want dit was niet op te halen uit lijst
maxweight = 9500 

x = input("all or search now: ")
x = x.casefold()

y = 0 


for item in datacol["results"]:
    
    slect = datacol["results"][y] #nested data om gegevens op te halen van specifieke pokemon
    name = slect["name"]

    if(x == "all"):
 
        url2 = "https://pokeapi.co/api/v2/pokemon/" + name #nested link voor andere gegevens
        print(url2)

        response2 = requests.get(url2) #zelfde proces als ophalen andere api gegevens
        jsonp2 = response2.json()

        datacol2 = json.loads(response2.text)

        print(name + " base experience: ", datacol2["base_experience"]) #eerste zoektfunctie, zoekt door middel van de input value door hele bestand
        
        for types in range(len(datacol2["types"])): #omdat niet elke pokemon 2 types moeten deze eerst geteld worden

            print(" type: " + datacol2["types"][types]["type"]["name"]) #naam van type it 4 lagen diep

        collectivebase.append(datacol2["base_experience"]) #berekening base exp voor matplotlib graph
        

    elif(x in name): #vergelijkbaar met vorige zoekfunctie. Zoekt specifiek op naam en berekent weight distribution
       
        print(slect)
        url2 = "https://pokeapi.co/api/v2/pokemon/" + x
        print(url2)

        response2 = requests.get(url2)
        jsonp2 = response2.json()

        datacol2 = json.loads(response2.text)
        
        print("good result: " + datacol2["name"] + " weight: ", datacol2["weight"])
        
        for types in range(len(datacol2["types"])):

            print(" type: " + datacol2["types"][types]["type"]["name"])

        
        z = np.array([minweight, datacol2["weight"], maxweight])  
        omega = ["Ghastly", datacol2["name"], "Groudon"]
        
        plt.bar(omega, z)       
        
    y += 1

np.array(collectivebase)
plt.hist(collectivebase)  
plt.show()

        
    
    

