# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup as bs
import requests as re
#%%
#link to get the list of all the cricketers ever played
link=re.get("https://en.wikipedia.org/wiki/List_of_One_Day_International_cricketers")
#%%
soup = bs(link.content, "html.parser")
#%%
#finding all the different countries ever played
d=soup.find_all(attrs={"class":"toctext"})
countries=[]
for i in d:
    countries.append(i.text)
    
print("the total number of countries ever played ODI are ", len(countries))

#%%
#finding all the cricketers per country
sections=soup.find_all("small")

player_country=[]
for i in sections:
    pp=i.text
    p=pp.splitlines()
    for j in p:
        player_country.append(j[:-2])
        
#%%
print("the total number of players ever played ODI International were: ",len(player_country))

#%%
#writing the players in a csv file
import pandas as pa
players=pa.DataFrame(player_country)

with open("player.csv","w") as f:
    players.to_csv(f)

#%%
#creating a seperate function for making batch wise requests, where each batch is of size 20
#also at the end of the processing, writing the retreived data in a file in json format.


def scrape(start, end,f):
    datad= data[start:end]
    for i in datad:
        text="performance analysis "+i+" howstat odi"
        url="https://www.google.co.in/search?q="+text
        link=re.get(url)
        if link:
            print("TRUE")
            print("\n\n")
            soup=bs(link.text,"html.parser")
            lin=soup.select_one("a[href*=PlayerYears_ODI]")
            info={}
            if lin!=None:
            
                print("\n\n\n")
                new_link=lin
                nl=new_link['href']   
                print("\n\n")
                ml=nl.replace("%3F","?")
                ml=(ml.replace("%3D","="))[7:]
                print(ml)
                
                next_page=re.get(ml)
                if next_page:
                    print("TRUE")
                soup2=bs(next_page.content,"html.parser")
                print("\n\n\n\n\n\n\n\n\n")
                x=soup2.find("div",attrs={"id":"bat"})
                    
                j=0
                year=x.find_all("a")
                for tr in x.find_all('tr')[2:-1]:
                    tds = tr.find_all('td')
                #    print(year[j].text+":::::::::"+str(tds[8])+"\n\n\n")
                    info[year[j].text]=int(tds[8].text.strip())
                    j+=1
                
                print(info)
            else:
                pass
            
            player_info[i]=info
                
        else:
            print("FALSE")
            print("\n\n")
            pass
        
        
    print(player_info)
    
    json.dump(player_info,f)


#%%
#===============================FINAL CODE====================================
import pandas as pa

df=pa.read_csv("player.csv")
data=df.iloc[:,1]

player_info={}


import json
f=open("final_data.json","a")

length=len(data)
start=end=0
while end<length:
    start=end
    if(start+20<=length-1):
        end=start+20
    else:
        end=length-1


    scrape(start,end,f)
    

#%%
#====================================TRIAL CODE================================== 
#play=['Virat Kohli']
#
#for i in play:
#    text="performance analysis "+i+" howstat"
#    url="https://www.google.co.in/search?q="+text
#    link=re.get(url)
#    if link:
#        print("TRUE")
#        print("\n\n\n")
#    else:
#        print("FALSE")
#        print("\n\n\n")
#    soup=bs(link.text,"html.parser")
#    lin=soup.select(".jfp3ef a")
#    
#        
#    print("\n\n\n")
#    new_link=lin[0]
#    nl=new_link['href']   
#    print("\n\n")
#    ml=nl.replace("%3F","?")
#    ml=(ml.replace("%3D","="))[7:]
#    print(ml)
#    
#    next_page=re.get(ml)
#    if next_page:
#        print("TRUE")
#    else:
#        print("FALSE")
#     
#next_page=re.get(ml)
#if next_page:
#    print("TRUE")
#else:
#    print("FALSE")
#        
#soup2=bs(next_page.content,"html.parser")
#print("\n\n\n\n\n\n\n\n\n")
#x=soup2.find("div",attrs={"id":"bat"})
#
#years=[]
#info={}
#j=0
#year=x.find_all("a")
#for tr in x.find_all('tr')[2:-1]:
#    tds = tr.find_all('td')
##    print(year[j].text+":::::::::"+str(tds[8])+"\n\n\n")
#    info[year[j].text]=tds[8].text.strip()
#    j+=1
#
#print(info)