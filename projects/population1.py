#Eg vann þetta verkefni með Johanni Inga i hop 2 

population = 307357870 #folksfjöldinn i Bandarikjunum

year = int(31536000) #sekundur a ari (365)

birth = year / 7 #fæðing a ari
death = year / 13 #dauðsfall a ari
new = year / 35 #nyr innflytjandi a ari

#breyting a folksfjölda ar hvert
new_population = birth - death + new


spurning = int(input("Years: "))


if spurning < 0:
    print("Invalid input!")

else:
    print("New population after",spurning,"years is",int(population + (new_population * spurning)))
    


    
