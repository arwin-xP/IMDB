import requests
import re
import json

def IMDBcode(x):
    r=requests.get('http://www.imdb.com/search/name?has=awards&name='+x)
    x=r.content
    c= ''.join(re.findall('/name/nm[0-9]{7}',x))
    x= c[21:30]
    return x

def top10(ans,x):
    if ans=='D':
        r=requests.get('http://www.imdb.com/filmosearch?explore=title_type&role='+x+'&ref_=filmo_ref_job_typ&mode=simple&page=1&title_type=movie&sort=user_rating,desc&job_type=director')
    else:
        if ans=='A':
            r=requests.get('http://www.imdb.com/filmosearch?explore=title_type&role='+x+'&ref_=filmo_ref_job_typ&mode=simple&page=1&title_type=movie&sort=user_rating,desc&job_type=actor')
        else:
            r=requests.get('http://www.imdb.com/filmosearch?explore=title_type&role='+x+'&ref_=filmo_ref_job_typ&mode=simple&page=1&title_type=movie&sort=user_rating,desc&job_type=actress')
    c= ' '.join(re.findall('filmo_li_tt"\n>[A-Z].*',r.content)).split('>')
    loop=range(1,len(c),2)
    t=[]
    for i in range(0,len(loop)):
        t.append(c[loop[i]])
    if len(loop)>10:
        for i in range(0,10):
            print t[i].split('<')[0]
    else:
        for i in range(0,len(loop)):
            print t[i].split('<')[0]
    print "\n" 
    
d='y'
while(d=='y'):
    name=raw_input("Enter person's full name to be searched (Check the spelling before entering): ")

    n=name.split(' ')
    if name!= n[0]:
        x=str(n[0]+"%20"+n[1])
    else :
        x=n[0]
    x=IMDBcode(x)
    ans=raw_input('Enter A for actors, C for actresses and D for director: ')
    top10(ans,x)
    d=raw_input("Do you want to retry? (y/n): ")
    
