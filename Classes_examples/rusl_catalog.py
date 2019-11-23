class Item:
   def __init__(self, name ="", category = ""):
      self.__name = name
      self.__category = category

   def set_name(self, other_name):
      self.__name = other_name

   def set_category(self, other_category):
      self.__category = other_category


   def __str__(self):
      return "Name: {}, Category: {}".format(self.__name, self.__category)

class Catalog:

   def __init__(self, name, collection = []):
      self.__name = name
      self.__collection = collection

   def add(self,item):
      self.__collection.append(item)


   def __str__(self):
      the_print = "Catalog {}:".format(self.__name)
      for item in self.__collection:
         the_print += str("\n\t{}".format(item))
      return the_print
 
#MAIN program starts here:
#from catalog import Item
#from catalog import Catalog
 
item1 = Item("Green Book", "Biography")
print(item1)
item2 = Item("The God", "Crime")
print(item2)
item2.set_name("The Godfather")
print(item2)
item3 = Item("Schindler's List", "Biography")
print(item3)
item3.set_category("Drama")
print(item3)
 
catalog = Catalog('Films')
catalog.add(item1)
catalog.add(item2)
catalog.add(item3)
print(catalog)