chess_dict = {"Carlsen": 2876,"Amand": 2765}
chess_list = []

for c in chess_dict.items():
   chess_list.append(list(c)) #convert the chess tuples to list

print(chess_list) #The original chess_dictionary with lists not tuples 

print(chess_dict.keys()) #Gets the keys in the dictionary


for key in chess_dict.keys(): #iterates over the keys and prints them out
   print("{} is a chess champion with {} points.".format(chess_dict.keys(),"2000"))

# for values in chess_dict.values(): #iterates over the values and prints them out
#    print(values)