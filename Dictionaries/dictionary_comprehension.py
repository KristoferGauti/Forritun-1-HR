a_dict = {k:v for k,v in enumerate('abcdefg')} 
print(a_dict,"\n")

b_dict = {v:k for k,v in a_dict.items()}
print(b_dict,"\n")
print(sorted(b_dict),"\n")

b_list = [(v,k) for v,k in b_dict.items()] 
print(sorted(b_list),"\n")

a_set = {ch for ch in'to be or not to be'} #set of unique characters
print(a_set)