for x in range(7):
    for y in range(x,7):
        print ("[",x,"|",y,"]",end=" ") #parametro end=" " para que no salte la línea 
    print()

teams = ['Dragons','Wolves','Pandas','Unicorns']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team, " VS ", away_team)