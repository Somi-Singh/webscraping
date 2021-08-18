import requests
import json
import os
from task1 import scrape_top_list
from task4 import scrape_movie_details
movie = scrape_top_list()

def get_movie_list_details():
    movie_list = []
    for i in movie:
        path = "/home/navgurukul/Desktop/webscraping/allmovies.text" + i["Name"] + ".text"
        if os.path.exists("file.json"):
            pass
        else:
            create = open("/home/navgurukul/Desktop/webscraping/allmovies.text" + i["Name"] + ".text","w")
            url = requests.get(i["Url"])
            create1 = create.write(url.text)
            create.close()
            a = scrape_movie_details(i["Name"],i["Url"])
            movie_list.append(a)
        with open("webscrap5.json","w+") as file5:
            json.dump(movie_list,file5,indent = 4)
            print(movie_list)
get_movie_list_details()