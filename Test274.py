import requests
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot

url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)
jsonp = response.json()

dataCol = json.loads(response.text)

df = pd.DataFrame(jsonp)

df.to_csv('PokeOutput.csv', encoding='utf-8', index=False)

#print(dataCol) 

x = input('search now: ')
y = 0

for item in dataCol["results"]:
    slect = dataCol["results"][y]
    name = slect["name"]
    #print(slect)
    if x in name:
        slectPok = dataCol["results"][y]
        print(slectPok)
          
    
    y += 1

