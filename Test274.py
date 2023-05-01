import requests
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



urlpoke = "https://pokeapi.co/api/v2/pokemon?limit=721&offset=0"
response = requests.get(urlpoke)
jsonp = response.json()

dataCol = json.loads(response.text)

df = pd.DataFrame(jsonp)

df.to_csv('PokeOutput.csv', encoding='utf-8', index=False)

collectivebase = [] 

minweight = 1
maxweight = 9500

x = input('all or search now: ')
x = x.casefold()
y = 0


for item in dataCol["results"]:
    slect = dataCol["results"][y]
    name = slect["name"]

    
    
    if(x == "all"):
 
        url2 = "https://pokeapi.co/api/v2/pokemon/" + name
        print(url2)

        response2 = requests.get(url2)
        jsonp2 = response2.json()

        dataCol2 = json.loads(response2.text)

        print(name + " base experience: ", dataCol2["base_experience"]) 
        for types in range(len(dataCol2["types"])):

            print(" type: " + dataCol2["types"][types]["type"]["name"])

        collectivebase.append(dataCol2["base_experience"]) #eerste berekening, wel af
        

    elif( x in name):
        print(slect)
        url2 = "https://pokeapi.co/api/v2/pokemon/" + x
        print(url2)

        response2 = requests.get(url2)
        jsonp2 = response2.json()

        dataCol2 = json.loads(response2.text)
        
        print('good result: ' + dataCol2["name"] + " weight: ", dataCol2["weight"])
        for types in range(len(dataCol2["types"])):

            print(" type: " + dataCol2["types"][types]["type"]["name"])

        
        z = np.array([minweight, dataCol2["weight"], maxweight])  #min en max weight opgezocht want dit was niet op te halen
        omega = ["Ghastly", dataCol2["name"], "Groudon"]
        plt.bar(omega, z)       
        
    y += 1

np.array(collectivebase)
plt.hist(collectivebase)  
plt.show()

        
    
    

