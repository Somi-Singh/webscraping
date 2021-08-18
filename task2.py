from  task1 import movie_data
import json
file =  open("webscrap1.json","r")
data = json.load(file)
print(data)

def group_by_year(movie):
    dic = {}
    for i in data:
        top_movie_list= []
        year = i["Year"]
        if year not in dic:
            for key in data:
                if year == key["Year"]:
                    top_movie_list.append(key)
            dic[year] = top_movie_list
    with open("webscrap2.json","w+") as file:
        json.dump(dic,file,indent = 4)
        a = json.dumps(dic)
year_ = group_by_year(movie=movie_data)