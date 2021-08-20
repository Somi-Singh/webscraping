import json
with open("webscrap5.json","r")as f:
    data = json.load(f)

def analyse_movie_director(data):
    dic1={}
    list_lan=[]
    for i in data:
        for j in i["director"]:
            if j not in dic1.keys():
                c=0
                for z in data:
                    for k in z["director"]:
                        if j==k:
                            c+=1
                dic1[j]=c   
    with open("webscrap7.json","w+") as director_data:
        json.dump(dic1,director_data,indent = 4)
    # print(director_dict)     
analyse_movie_director(data)

