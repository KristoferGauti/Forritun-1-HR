print("Looping over a range of numbers")
for i in [0,1,2,3,4,5]:
    print(i**2)

print()

print("Looping over a list and print its values")
colors = ["red","green","blue","yellow"]

for color in colors:
    print(color)

print()

print("Looping backwards")
for color in reversed(colors):
    print(color)
    
print()

print("Looping over a collection and indicies")
for i, x in enumerate(colors, start=1):
    print(i,x)

print()

print("Looping over two collection")
names = ["Raymond","Rachel","Matthew","Joe"]
colors = ["red","green","blue","yellow"]

for name, color in zip(names,colors):
    print(name,"-->",color)

print()

print("looping in sorted order")
colors = ["red","green","blue","yellow"]


for color in sorted(colors, reverse = True):
    print(color)

print()

#********************************************************************************
print("Looping over directionary keys and items")
d = {"Matthew":"blue","Rachel":"green","Raymond":"Red"}

for k in d:
    print(k)

for k, v in d.items():
    print(k,"-->",v)

print("Construct a dictionary from two list")

names = ["Raymond","Rachel","Matthew","Joe"]
colors = ["red","green","blue","yellow"]

d = dict(zip(names,colors))
print(d)



    
    
    
