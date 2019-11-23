# Algorithm for top 100 chess players

# Að lesa inn skrá 
# Að vinna úr skrá
# Dictionary eða tuple 
# Name => rank, country, elo, b-day       csv_skjöl/chess-top-100.csv

def open_file(filename):
   try:
      file_stream = open(filename,"r")
      return file_stream

   except FileNotFoundError:
      return None

def create_player_dict(file_stream):
   dict_players = {}

   for line in file_stream:
      rank, name, country, rating, bday = line.strip().split("; ")

      name = name.strip()
      country = country.strip()
      last_name, first_name = name.split(", ")

      key = "{} {}".format(first_name, last_name)
      dict_players[key] = (int(rank), country, int(rating), int(bday))
   return dict_players

def create_countries_dict(dict_players):
   dict_countries = {}
   people_list = []

   for a_tuple in dict_players.items():
      country = a_tuple[1][1]
      people = a_tuple[0]
      rating = a_tuple[1][2]

      if country in dict_countries:
         dict_countries[country] += (people, rating),
      else:
         dict_countries[country] = (people, rating),

   return dict_countries

def clean_dict_countries(dict_countries):
   clean_list = []
   

   for a_tuple in dict_countries.items():
      country = a_tuple[0]
      count_people = len(a_tuple[1])

      total = []
      for b_tuple in a_tuple[1]:
         score = b_tuple[1]
         total.append(score)
      avr = sum(total)/count_people
      
      
      clean_list.append((country,(count_people),avr))

   return clean_list


def print_sorted(dict_countries, dict_players, clean_dict_countries):
   #print(country, rank, rating)
   #print("{:>40}{:>10d}".format(a_tuple))

   sorted_list = sorted(clean_dict_countries)

   for x in sorted_list:
      country = x[0]
      number = x[1]
      avr = x [2]
      print("{} ({}) ({:.1f}):".format(country,number,avr))

      for item in dict_countries[country]:
         name = item[0]
         rating = item[1]
         print("{:>40}{:>10d}".format(name, rating))
      


def print_header(title):
   print(title)
   print("-------------------")

def main():
   file_name = input("Enter filename: ")

   file_stream = open_file(file_name)

   if file_stream:
      dict_players = create_player_dict(file_stream)
      
      dict_countries = create_countries_dict(dict_players)

     
      
      print_header("Players by country:")
      dictionary = clean_dict_countries(dict_countries)

      print_sorted(dict_countries, dict_players, dictionary)


main()
