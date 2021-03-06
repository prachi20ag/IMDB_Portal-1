import requests
import os
import sys
import json
import bs4


os.system('clear')


status=open('info.txt','a')



def info_movie():
    name=raw_input('\nEnter the title of the movie: ')
    t=name.replace(' ','+')
    x=raw_input("\nDo you know the year of release?If yes, type 'Yes'/'Y'/'y', else press any button to continue! ")
    if (x=='Yes') or (x=='Y') or (x=='y'):
        y=input("\n\nEnter the year: ")
    else:
        y=""
    url='http://www.omdbapi.com/?t='+str(t)+'&y='+str(y)+'&plot=short&r=json'
    response=requests.get(url)
    w = json.loads(response.text)
    try:
      title=w['Title']
      rating=w['imdbRating']
      cast=w['Actors']
      year= w['Released']
      genre=w['Genre']
      language= w['Language']
      director = w['Director']
      duration=w['Runtime']
      plot= w['Plot']
      print ("\n\n----------------------------MOVIE INFORMATION-------------------------\n")
      print ("\n\t TITLE       : \t\t"+title)
      print ("\n\t IMDB RATING : \t\t"+rating)
      print ("\n\t RELEASED ON : \t\t"+year)
      print ("\n\t DURATION    : \t\t"+duration)
      print ("\n\t LANGUAGE    : \t\t"+language)
      print ("\n\t GENRE       : \t\t"+genre)
      print ("\n\t DIRECTOR    : \t\t"+director)
      print ("\n\t CAST        : \t\t"+cast)
      print ("\n\t PLOT        : \t\t"+plot)
      
      status.write ("\n\n--------------------------------------MOVIE INFORMATION---------------------------------\n")
      status.write ("\n\t TITLE       : \t\t"+title)
      status.write ("\n\t IMDB RATING : \t\t"+rating)
      status.write ("\n\t RELEASED ON : \t\t"+year)
      status.write ("\n\t DURATION    : \t\t"+duration)
      status.write ("\n\t LANGUAGE    : \t\t"+language)
      status.write ("\n\t GENRE       : \t\t"+genre)
      status.write ("\n\t DIRECTOR    : \t\t"+director)
      status.write ("\n\t CAST        : \t\t"+cast)
      status.write ("\n\t PLOT        : \t\t"+plot)
    except KeyError:
        print "\nNo such movie titled '"+name+"' found or else read the instructions before using this feature!\n"
        status.write ("\nNo such movie titled '"+name+"' found else read the instructions before using this feature!\n")
    
    
def top_movies():
    x=input("\nEnter n, to display Top 'n' movies: " )
    url='http://www.imdb.com/chart/top'
    response=requests.get(url)
    html=response.text
    soup=bs4.BeautifulSoup(html,"lxml")
    rows=soup.select('.lister-list tr')
    #print rows[26]
    print ("\n"+"----------------------------------TOP "+str(x)+" MOVIES ACCORDING TO IMDB RATINGS---------------------------------"+"\n\n")
    print (" \t   TITLE\t\t\t\t\t\t\t\t\t\t   IMDB RATING\n\n")
    status.write ("\n"+"---------------------------TOP "+str(x)+" MOVIES ACCORDING TO IMDB RATINGS-----------------------------"+"\n\n")
    status.write (" \t   TITLE\t\t\t\t\t\t\t\t\t\t   IMDB RATING\n\n")
    
    for row in range(0,x):
        tdata=rows[row].select('td')
        name=tdata[1].get_text(' ',strip=True)
        rating=tdata[2].get_text(' ',strip=True)
        ans=("\n "+name.ljust(75,' ')+"\t\t\t\t"+rating+"\n")
        ans=ans.encode('ascii','ignore')
        print ans
        status.write (ans)
        
        
def folder():
    
    path=raw_input("\n\nEnter the complete path of the directory where your movies are present: ")
    dirs=os.listdir(path)
        
    for i in range(len(dirs)):
        x=dirs[i]
        t=x.replace(' ','+')
        url='http://www.omdbapi.com/?t='+str(t)+'&y=&plot=short&r=json'
        response=requests.get(url)
        w = json.loads(response.text)
        try:
            title=w['Title']
            rating=w['imdbRating']
            year= w['Year']
            x=path+x
            x=x.encode('ascii','ignore')
            ans="["+rating+"] "+title+" ("+year+")"
            ans=ans.encode('ascii','ignore')
            print "\n"+ans
            status.write ("\n"+ans)
            ans=path+ans
            os.rename(x,ans)
            print "Renaming Done\n"
            status.write ('Renaming Done\n')
            
        except KeyError:
            print "\nNo such movie titled '"+x+"' found or else read the instructions before using this feature!\n"
            status.write ("\nNo such movie titled '"+x+"' found else read the instructions before using this feature!\n")
    
    
    

def driver():
    print "\n\n\t\t\t\t\t------------------------------------------------IMDB PORTAL------------------------------------------------"
    status.write("\\\n\n\t\t\t\t\t------------------------------------------------IMDB PORTAL------------------------------------------------")
    choice=input('Enter your choice:\n\n1) Search movie information by title\n2) Show top rated movies\n3) Rename folder with IMDB rating and year of release added to it\n\nInput: ')
    
    if(choice==1):
        info_movie()
    elif(choice==2):
        top_movies()
    else:
            folder()
            
        
driver()
while (1>0) :
    repeat=raw_input("\n\nDo you want to try again (Type 'Yes'/'Y'/'y' or else press anything)? ")
    if (repeat=='Yes') or (repeat=='Y') or (repeat=='y'):
        os.system('clear')
        driver()
    else:
        print "\nThank you for using!"
        status.write("\nThank you for using!")
        break

status.close()

