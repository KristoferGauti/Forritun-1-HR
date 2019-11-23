class Item:
   """The parent class contains name of the 
   items and name of the category"""

   def __init__(self, name, category):
      """Private variables so that the user cannot 
      access those variables in the main application"""
      self.__name = name
      self.__category = category

   def __str__(self):
      return "Name: {}, Category: {}".format(self.__name, self.__category)

   def set_name(self, new_name):
      self.__name = new_name

   def set_category(self, new_category):
      self.__category = new_category

class Catalog:
   """item_list is a class variable that contains 
   all the items that the user has put. The user 
   can add to the list, find items, remove items and so on"""

   def __init__(self, name, collections = []):
      self.__name = name
      self.__collections = collections

   def __str__(self):
      the_print = "Catalog {}:".format(self.__name)
      the_print += "".join("\n\t{}".format(item) for item in self.__collections)
      return the_print

   def add(self, item):
      self.__collections.append(item)

   def remove(self, to_be_removed):
      if to_be_removed in self.__collections:
         self.__collections.remove(to_be_removed)

   def set_name(self, new_name):
      self.__name = new_name

   def find_item_by_name(self, find_item):
      for x in range(len(self.__collections)):
         if find_item in str(self.__collections[x]):
            return str(self.__collections[x])

   def clear(self):
      self.__collections = []
      return self.__collections



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

catalog.remove(item2)
print(catalog)

catalog.set_name("Favorite Movies")
print(catalog)

print(catalog.find_item_by_name("Green Book"))
print(catalog.find_item_by_name("The Godfather"))

catalog.clear()
print(catalog)
