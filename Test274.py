import requests
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

z = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(z, np.sin(z))       # Plot the sine of each x point
plt.show()                   # Display the plot

url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)
jsonp = response.json()

dataCol = json.loads(response.text)

df = pd.DataFrame(jsonp)

df.to_csv('PokeOutput.csv', encoding='utf-8', index=False)

#print(dataCol) 

x = input('search now: ')
x = x.casefold()
y = 0

for item in dataCol["results"]:
    slect = dataCol["results"][y]
    name = slect["name"]
    
    #print(slect)
    if x in name:
        slectPok = dataCol["results"][y]
        print(slectPok)
        url2 = "https://pokeapi.co/api/v2/pokemon/" + x
        print(url2)

        response2 = requests.get(url2)
        jsonp2 = response2.json()

        dataCol2 = json.loads(response2.text)
        
        """x2 = input('search now: ')
        x2 = x2.casefold()
        y2 = 0

        slect2 = dataCol2["results"][y2]"""
        print(dataCol2)
        
    
    y += 1

