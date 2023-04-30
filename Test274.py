import requests
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)
jsonp = response.json()

dataCol = json.loads(response.text)

df = pd.DataFrame(jsonp)

df.to_csv('PokeOutput.csv', encoding='utf-8', index=False)

collectivebase = []  # Create a list of evenly-spaced numbers over the range
                  # Display the plot


x = input('search now: ')
x = x.casefold()
y = 0

for item in dataCol["results"]:
    slect = dataCol["results"][y]
    name = slect["name"]
    
    #print(slect)
    if(x == "all"):
        
        print(name)

        url2 = "https://pokeapi.co/api/v2/pokemon/" + name
        print(url2)

        response2 = requests.get(url2)
        jsonp2 = response2.json()

        dataCol2 = json.loads(response2.text)

        collectivebase.append(dataCol2["base_experience"])
        

    elif( x in name):
        print(slect)
        url2 = "https://pokeapi.co/api/v2/pokemon/" + x
        print(url2)

        response2 = requests.get(url2)
        jsonp2 = response2.json()

        dataCol2 = json.loads(response2.text)
        #print(dataCol2["stats"][0]["base_stat"])
        
        """x2 = input('search now: ')
        x2 = x2.casefold()
        y2 = 0

        slect2 = dataCol2["results"][y2]"""
        print('good result: ' + dataCol2["name"] + " type1: " + dataCol2["types"][0]["type"]["name"] + " type2: " + dataCol2["types"][1]["type"]["name"])

        z = np.array([0, dataCol2["weight"], 100])  # Create a list of evenly-spaced numbers over the range
                  # Display the plot
        plt.plot(z, marker = 'o')       # Plot the sine of each x point
        
    y += 1

np.array(collectivebase)
plt.hist(collectivebase)       # Plot the sine of each x point
plt.show()

        
    
    

