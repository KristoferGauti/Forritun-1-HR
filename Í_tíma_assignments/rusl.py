def open_file(file_name):
    try:
        file_stream = open(file_name, 'r')
        return file_stream
    except FileNotFoundError:
        return None

def create_players_dict(file_stream):
    dict_players = {}
    for line in file_stream:
        rank, name, country, rating, bday = line.strip().split('; ')

        name = name.strip()
        country = country.strip()
        last_name, first_name = name.split(', ')

        key = '{} {}'.format(first_name, last_name)
        dict_players[key] = (int(rank), country.strip(), int(rating), int(bday))
    
    return dict_players


def create_birthday_dict(dict_players):
    dict_bday = {}
    for a_tuple in dict_players.items():
            bday = a_tuple[1][3]
            rating = a_tuple[1][2]
            name = a_tuple[0]
            if bday in dict_bday:
                dict_bday[bday] += (name, rating),
            else:
                dict_bday[bday] = (name, rating),
    return dict_bday

def clean_up_countries_dict(dict_countires):
    list1 = []
    for a_tuple in dict_countires.items():
        bday = a_tuple[0]
        nr_of_people = len(a_tuple[1])
        total_score = 0
        for b_tuple in a_tuple[1]:
            score = b_tuple[1]
            total_score += score
        avr_score = total_score / nr_of_people
        list1.append((bday, "({})".format(nr_of_people), "({:.1f})".format(avr_score)),)
    list1 = sorted(list1)
    return list1

def sort_dict(a_dict):
    return sorted(list(a_dict))


def print_sorted(list1, dict_countires):
    for x in list1:
        bday = x[0]
        nr = x[1]
        avr = x[2]
        print("{} {} {}:".format(bday, nr, avr))

        sort_dict(dict_countires)

        for item in dict_countires[bday]:
            name = item[0]
            rating = item[1]
            print("{:>40}{:>10d}".format(name, rating))

def print_header(title):
    print(title)
    print('-'*len(title))

def clean_up_countries_dict(dict_countires):
    list1 = []
    for a_tuple in dict_countires.items():
        country = a_tuple[0]
        nr_of_people = len(a_tuple[1])
        total_score = 0
        for b_tuple in a_tuple[1]:
            score = b_tuple[1]
            total_score += score
        avr_score = total_score / nr_of_people
        list1.append((country, "({})".format(nr_of_people), "({:.1f})".format(avr_score)),)
    list1 = sorted(list1)
    return list1

def create_countries_dict(dict_players):
    dict_countries = {}
    for a_tuple in dict_players.items():
            country = a_tuple[1][1]
            rating = a_tuple[1][2]
            name = a_tuple[0]
            if country in dict_countries:
                dict_countries[country] += (name, rating),
            else:
                dict_countries[country] = (name, rating),
    return dict_countries

def main():
    file_name = input('Enter filename: ')
    file_stream = open_file(file_name)
    if file_stream:
        dict_players = create_players_dict(file_stream)

        print_header('Players by country:')
        dict_countries = create_countries_dict(dict_players)
        list1 = clean_up_countries_dict(dict_countries)
        print_sorted(list1, dict_countries)

        print_header('Players by birth year:')
        dict_bday = create_birthday_dict(dict_players)
        list1 = clean_up_countries_dict(dict_bday)
        print_sorted(list1, dict_bday)

main()