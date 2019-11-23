
def vector_size(dimention):
   element_list = []
   for x in range(1,(dimention * 2)+1):
      element = int(input("element number {}: ".format(x)))
      element_list.append(element)




   



def main():
   dim = int(input("Input vector size: "))
   vector_size(dim)

main()