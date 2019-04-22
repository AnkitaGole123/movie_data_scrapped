
def group_by_year(movies):
    years = []
    for i in movies:
        year = i["year"]
        if year not in years:
            years.append(year)
        movie_dic = {i:[]for i in years}
        for i in movies:
            years = i['year']
            for x in  movie_dic:
                if str(x) == str(year):
                    movie_dic[x].append(movies[i])
    return movie_dic
task2 = group_by_year()
print (task2)