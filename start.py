import pandas
import matplotlib.pyplot as plt
import numpy as np

mijnbestand = pandas.read_csv("Pokemon.csv", na_filter=False)

z = np.linspace(0, 2)  # Create a list of evenly-spaced numbers over the range


#print(mijnbestand.columns)

x = input('search name of Pokemon or Move: ')

for index, pokemon in mijnbestand.iterrows():
    if (x.casefold() == "all"):
        print(pokemon["Name"], pokemon["Type 1"], pokemon["Type 2"])
    else:
        if(x in pokemon["Name"]):
            print(pokemon["Name"], pokemon["HP"])
            z += pokemon["HP"]
            
        if (x in pokemon["Type 1"] or x in pokemon["Type 2"]):
            print(pokemon["Name"], pokemon["Type 1"], pokemon["Type 2"])

plt.plot(z, np.sin(z))       # Plot the sine of each x point
plt.show() 
    
        