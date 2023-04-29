import pandas
import matplotlib.pyplot as plt
import numpy as np

import random

mijnbestand = pandas.read_csv("Pokemon.csv", na_filter=False)

z = np.linspace(0, 2)  # Create a list of evenly-spaced numbers over the range


#print(mijnbestand.columns)
start = input('search, stats, random or (random) fight? ')

if(start == "search"):
    search = input('Show all or search name of Pokemon/Move or legendary: ')

    for index, pokemon in mijnbestand.iterrows():
        if (search.casefold() == "all"):
            print(pokemon["Name"], pokemon["Type 1"], pokemon["Type 2"])
        elif (search.casefold() == "legendary"):
            if(pokemon["Legendary"]):
                print(pokemon["Name"], "Legendary")
        else:
            if(search in pokemon["Name"] or search.casefold() in pokemon["Name"]):
                print(pokemon["Name"], pokemon["HP"])
                z += pokemon["HP"]
                
            if (search in pokemon["Type 1"] or search in pokemon["Type 2"] or search.casefold() in pokemon["Type 1"] or search.casefold() in pokemon["Type 2"]):
                print(pokemon["Name"], pokemon["Type 1"], pokemon["Type 2"])
        
        

    plt.plot(z, np.sin(z))       # Plot the sine of each x point
    plt.show() 

elif (start == 'stats'):
    totalHP = 0
    for index, pokemon in mijnbestand.iterrows():
        totalHP = totalHP + pokemon["HP"]
        print(totalHP)

elif(start == 'random'):
    from random import *
    num = randint(1, 802)
    
    for index, pokemon in mijnbestand.iterrows():
        if (num == pokemon["#"]):
            print(pokemon["Name"])

elif(start == 'fight'):
    from random import *
    num = randint(1, 802)
    num2 = randint(1, 802)

    pok1 =  mijnbestand[mijnbestand["#"] == num]
    pok2 =  mijnbestand[mijnbestand["#"] == num2]

    pok1stats = pok1["Total"]
    pok2stats = pok2["Total"]

    if pok1(pok1):
     print(pok1stats, pok2stats)
    
    """for index, pokemon in mijnbestand.iterrows():    
        if (num == pokemon["#"]):
            p = pokemon["HP"]
            print(pokemon["Name"], p)
        if (num2 == pokemon["#"]): 
            p2 = pokemon["HP"]
            print(pokemon["Name"], p2)"""
                  

        

        
        