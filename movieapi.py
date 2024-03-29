import requests
def movieinfo(mvtitle,year):
 url=f"http://www.omdbapi.com/?t={mvtitle}&y={year}=/&apikey=a08e67c4"
 response=requests.get(url)
 if response.status_code==200:
    details = dict(response.json())
    name=details["Title"]
    dir=details["Director"]
    rel=details["Released"]
    gen=details["Genre"]
    rate=details["imdbRating"]
    box=details["BoxOffice"]
    pos=details["Poster"]
    det={"Title":name,"Director":dir,"Release Year":rel,"Genre":gen,"IMDb Rating":rate,"Box Office":box,"Poster":pos}
 return det



