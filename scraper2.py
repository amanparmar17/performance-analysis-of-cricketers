#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:25:35 2019

@author: aman
"""

import json

with open("scores.json","r") as f:
    data=json.load(f)

#%%
    
player=input("Please enter the name of the player you want information about: ")
player=player.title()
info=data[player]

#%%
#summarising the information of the player

years=list(map(int,info.keys()))
start=min(years)
end=max(years)

print("Player name: ",player)
print("Started in: ",str(start))
print("Ended playing in: ",str(end))
#%%
#function to cumulify the scores
def cumulify(year):
    index=years.index(int(year))
    scores=0
    for i in range(0,index+1):
        key=str(years[i])
        scores+=info[key]
    return scores



#%%

choice=int(input("Please select:\n1- To knwo the runs scored in a single year of choice \n2- To know the cumulative runs\n"))

print("PLEASE ENTER THE YEARS BETWEEN {0} AND {1}".format(start,end))
        
        
if choice==1:
    target_year=(input("\nPlease enter the year you want ot know the runs scored: "))
    runs_scored=info[target_year]
    print("The runs scored in the year {0} are: {1}".format(target_year,runs_scored))
elif choice==2:
    ye=int(input("\nPlease enter the year you want to know the cumulative runs scored: "))
    runss=cumulify(ye)
    print("The runs scored till date are: ",str(runss))
else:
    print("Entered an invalid choice")




