# Performance-analysis-of-cricketers

## Work to be done:
* Crawl all the players ever played ODI International cricket
* Find the runs scored by these players in there career, year wise
* Cumulify the runs as per the year entered by the user

## Packages used:
* Beautiful Soup
* Requests
* Json
* Pandas


## Solution:
* The list of cricketers ever played ODI cricket is gathered by crawling the wikipedia page of the same.
  * The link is:
    * https://en.wikipedia.org/wiki/List_of_One_Day_International_cricketers
* The crawled cricketers are saved in a separate csv file
* To get the list of the runs scored by the players
  * Site used:
    * HOWSTAT
  * Link:
    * http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID=3600
    * Here change the last id according to the player of interest
* To get the same result for each of the players,
  * Created a general search query 
    * text="performance analysis "+i+" howstat", i is the name of the cricketer 
  * Searched the google for each custom query created
  * Crawled the search result page for a link with particular keyword,i.e, “PlayerYears_ODI”
    lin=soup.select_one("a[href*=PlayerYears_ODI]")
* Customised the link retreived
* Propogated through the link and crawled the result page
* Created a dictionary, by crawling the table on the resulting page, of the year and the runs scored in that year
* Crawled the data for all the players and stored the final result in the form of a dictionary in a json file.
                                  
* To finalise the query of the user for the runs:
  * Loade the json 
  * Take input from the user for the target player
  * Find the result from the dictionary for the player show the result by calculating the total runs as per the year entered

Below are some screenshots proving the working of the code

![alt text](https://github.com/amanparmar17/performance-analysis-of-cricketers/blob/master/Screenshot%20from%202019-05-30%2020-18-22.png)

<br><br>
![alt text](https://github.com/amanparmar17/performance-analysis-of-cricketers/blob/master/Screenshot%20from%202019-05-31%2001-35-11.png)
<br><br>
![alt text](https://github.com/amanparmar17/performance-analysis-of-cricketers/blob/master/Screenshot%20from%202019-05-31%2002-01-55.png)
<br><br>
![alt text](https://github.com/amanparmar17/performance-analysis-of-cricketers/blob/master/Screenshot%20from%202019-05-31%2002-19-40.png)
<br><br>
![alt text](https://github.com/amanparmar17/performance-analysis-of-cricketers/blob/master/Screenshot%20from%202019-05-31%2002-20-04.png)
