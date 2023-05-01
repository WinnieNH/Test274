import pandas
import matplotlib.pyplot as plt
import numpy as np

import random

pokebestand = pandas.read_csv("Pokemon.csv", na_filter=False)
ACbestand = pandas.read_csv("Villagers.csv", na_filter=False)

z = np.linspace(0, 2)  

HPcalc = []

start = input('AC or Pokemon: search, stats, random or (random) fight? ')

if(start == "AC"):
    print(ACbestand["Name"])
elif(start == "search"):
    search = input('Show all or search name of Pokemon/Move or legendary: ')

    for index, pokemon in pokebestand.iterrows():
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
        
        

    plt.plot(z, np.sin(z))       
    plt.show() 

elif (start == 'stats'):
    totalHP = 0
    for index, pokemon in pokebestand.iterrows():
        totalHP = totalHP + pokemon["HP"] #eerste berekening, wel af
        print("totalHP: ", totalHP)

        HPcalc.append(pokemon["HP"])
        plt.hist(HPcalc)
    plt.show()    
    
elif(start == 'random'):
    from random import *
    num = randint(1, 802)
    
    for index, pokemon in pokebestand.iterrows():
        if (num == pokemon["#"]):
            print(pokemon["Name"])

elif(start == "fight"): #TWEEDE BEREKENING DIE NOG AF MOET!
    from random import *
    num = randint(1, 802)
    num2 = randint(1, 802)

    for index, pokemon in pokebestand.iterrows():
        if(num == pokemon["#"]):
            pok1stats = pokemon["Total"]
            pok1name = pokemon["Name"]
    for index, pokemon in pokebestand.iterrows():
        if (num2 == pokemon["#"]):
            pok2stats = pokemon["Total"]
            pok2name = pokemon["Name"]
               


    print(pok1name, pok1stats)
    print(pok2name, pok2stats)
    if(pok1stats > pok2stats):
        print(pok1name + " wins")
    elif(pok1stats < pok2stats):
        print(pok2name + " wins")
    else:
        print("draw")     
                  

        

        
        